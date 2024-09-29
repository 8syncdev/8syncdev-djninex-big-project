from api_core.common.type import *
from django.utils import timezone

from api_core.dev import (
    #^ Async custom
    alist,
    sta,
    alist_model,
    afilter
)

from .model import *

from django.utils.timezone import timedelta, now

class CourseService:

    def __init__(self):
        self.course_model = Course
        self.chapter_model = Chapter
        self.lesson_model = Lesson
        self.user_enrollment_model = UserEnrollment
    
    async def get_courses(self):
        courses = await alist_model(self.course_model.objects.order_by('pk').all)
        formatted_courses = []
        for course in courses:
            formatted_course = {
                "title": course.name,
                "description": course.description,
                "duration": course.duration,
                "price": course.price,
                "image": course.img_url,
                "link": f"/course/{course.id}",
                "categories": course.categories
            }
            if course.voucher:
                formatted_course["originalPrice"] = course.price
                formatted_course["price"] = course.price * (1 - course.voucher.discount)
            else:
                voucher_50_percent = course.price * 0.5
                formatted_course["originalPrice"] = course.price
                formatted_course["price"] = course.price - voucher_50_percent
            formatted_courses.append(formatted_course)
        return formatted_courses
    
    async def get_course_content_json_by_id(self, course_id: int):
        course = await self.course_model.objects.aget(pk=course_id)
        return course

    async def get_chapters_of_course(self, course_id: int):
        chapters_of_course = await afilter(
            self.chapter_model.objects.prefetch_related('courses').order_by('pk').filter,
            courses__pk=course_id
        )
        return chapters_of_course
    
    async def get_user_enrollment_of_course(self, user: User, course_id: int):
        check_exist = await afilter(
            self.user_enrollment_model.objects.select_related('user', 'course').filter,
            user=user,
            course__pk=course_id
        )
        return check_exist[0] if check_exist.__len__() > 0 else None
    
    async def check_user_enrolled_course(self, user: User, course_id: int) -> bool:
        user_enrollment = await self.get_user_enrollment_of_course(user, course_id)
        if user_enrollment and user_enrollment.status in [UserEnrollment.STATUS_COMPLETED, UserEnrollment.STATUS_TRIAL]:
            if user_enrollment.status == UserEnrollment.STATUS_TRIAL:
                if user_enrollment.expiration_date >= timezone.now():
                    return True
                else:
                    user_enrollment.status = UserEnrollment.STATUS_EXPIRED
                    await user_enrollment.asave()
                    return False
            
            if user_enrollment.status == UserEnrollment.STATUS_COMPLETED:
                if user_enrollment.is_check_expiration:
                    if user_enrollment.expiration_date >= timezone.now():
                        return True
                    else:
                        user_enrollment.status = UserEnrollment.STATUS_EXPIRED
                        await user_enrollment.asave()
                        return False
                else:
                    return True
        else:
            return False


    async def get_lessons_of_chapter(self, chapter_id: int, user: User):
        # course_of_chapter = await self.chapter_model.objects.prefetch_related('courses').aget(pk=chapter_id)
        # try:
        #     find = await alist_model(course_of_chapter.courses.all)
        #     find_course: Course = find[0]
        #     check_enrolled = await self.check_user_enrolled_course(user, find_course.pk)
        #     if check_enrolled:
        #         lessons_of_chapter = await afilter(
        #             self.lesson_model.objects.prefetch_related('chapters').filter,
        #             chapters__pk=chapter_id
        #         )
        #         return lessons_of_chapter
        #     else:
        #         return []
        # except Exception as e:
        #     print(e)
        #     return []
        lessons_of_chapter = await afilter(
            self.lesson_model.objects.prefetch_related('chapters').order_by('pk').filter,
            chapters__pk=chapter_id
        )
        return lessons_of_chapter
    
    async def get_lesson_content(self, lesson_id: int, user: User):
        lesson_content = await self.lesson_model.objects.prefetch_related('chapters').aget(pk=lesson_id)
        if lesson_content.is_trial:
            return lesson_content
        chapters_of_course = await alist_model(lesson_content.chapters.all)
        if chapters_of_course.__len__() == 0:
            return
        chapters_of_course: Chapter = chapters_of_course[0]
        course_of_chapter = await alist_model(chapters_of_course.courses.all)
        if course_of_chapter.__len__() == 0:
            return
        course_of_chapter: Course = course_of_chapter[0]
        # lesson_content = await self.lesson_model.objects.aget(pk=lesson_id)
        check_enrolled = await self.check_user_enrolled_course(user, course_of_chapter.pk)
        if check_enrolled:
            return lesson_content
        else:
            return {
                'message': 'User not enrolled in this course'
            }
    
    async def enroll_course(self, user: User, course_id: int, status: str = UserEnrollment.STATUS_ENROLLED, is_trial: bool = False):
        user_enrollment, created = await self.user_enrollment_model.objects.aget_or_create(
            user=user,
            course=await self.course_model.objects.aget(pk=course_id),
        )
        if created or user_enrollment.status == UserEnrollment.STATUS_CANCELLED:
            if is_trial: #! controller should check is_trial before call this function, viết hàm controller để check is_trial
                user_enrollment.status = UserEnrollment.STATUS_TRIAL
                user_enrollment.expiration_date = now() + timedelta(minutes=UserEnrollment.EXPIRATION_TEST_MINUTES)
            else:
                user_enrollment.status = status
            await user_enrollment.asave()
            return {
                **user_enrollment.__dict__,
                'message': 'User enrolled in course'
            }
        if is_trial and user_enrollment.status == UserEnrollment.STATUS_ENROLLED:
            user_enrollment.status = UserEnrollment.STATUS_TRIAL
            user_enrollment.expiration_date = now() + timedelta(minutes=UserEnrollment.EXPIRATION_TEST_MINUTES)
            await user_enrollment.asave()
            return {
                **user_enrollment.__dict__,
                'message': 'User enrolled in course'
            }
        
        return {
            **user_enrollment.__dict__,
            'message': 'User already enrolled in this course'
        }
    
    async def get_user_enrollments(self, user: User):
        user_enrollments = await afilter(
            self.user_enrollment_model.objects.select_related('user', 'course').filter,
            user=user
        )
        return [
            {
                'course': user_enrollment.course.pk,
                'course_title': user_enrollment.course.name,
                'course_img_url': user_enrollment.course.img_url,
                'status': user_enrollment.status,
                'created_at': user_enrollment.created_at,
                'updated_at': user_enrollment.updated_at,
                'expiration_date': user_enrollment.expiration_date
            }
            for user_enrollment in user_enrollments
        ] if user_enrollments.__len__() > 0 else []
    
    async def get_all_user_enrollments(self):
        user_enrollments = await alist_model(
            self.user_enrollment_model.objects.select_related('user', 'course').all
        )
        return [
            {
                'course': user_enrollment.course.pk,
                'username': user_enrollment.user.username,
                'course_title': user_enrollment.course.name,
                'status': user_enrollment.status,
                'created_at': user_enrollment.created_at,
                'updated_at': user_enrollment.updated_at,
                'expiration_date': user_enrollment.expiration_date
            }
            for user_enrollment in user_enrollments
        ]
        
    async def delete_all_user_enrollments(self):
        await self.user_enrollment_model.objects.all().adelete()
        return {
            'message': 'All user enrollments deleted'
        }

    async def create_or_update_content_json_course(self, course_id: int, content_json: dict):
        course = await self.course_model.objects.aget(pk=course_id)
        course.content_json = content_json
        await course.asave()
        return course
        
