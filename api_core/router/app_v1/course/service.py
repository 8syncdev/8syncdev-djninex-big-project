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

class CourseService:

    def __init__(self):
        self.course_model = Course
        self.chapter_model = Chapter
        self.lesson_model = Lesson
        self.user_enrollment_model = UserEnrollment
    
    async def get_courses(self):
        courses = await alist_model(self.course_model.objects.all)
        return courses

    async def get_chapters_of_course(self, course_id: int):
        chapters_of_course = await afilter(
            self.chapter_model.objects.prefetch_related('courses').filter,
            courses__pk=course_id
        )
        return chapters_of_course
    
    async def check_user_enrollment(self, user: User, course_id: int):
        check_exist = await afilter(
            self.user_enrollment_model.objects.select_related('user', 'course').filter,
            user=user,
            course__pk=course_id
        )
        return check_exist[0]
    
    async def get_lessons_of_chapter(self, chapter_id: int, user: User):
        course_of_chapter = await self.chapter_model.objects.prefetch_related('courses').aget(pk=chapter_id)
        try:
            find = await alist_model(course_of_chapter.courses.all)
            find_object: Course = find[0]
            check_enrollment = await self.check_user_enrollment(user, find_object.pk)
            #^ Chưa check expiration_date
            if check_enrollment.status == UserEnrollment.STATUS_ENROLLED:
                if check_enrollment.expiration_date < timezone.now():
                    print('User already enrolled in this course')
                else:
                    check_enrollment.status = UserEnrollment.STATUS_CANCELLED
                    await check_enrollment.asave()
                    print('Expired')
            else:
                print('User not enrolled in this course')
                
        except Exception as e:
            print(e)
        lessons_of_chapter = await afilter(
            self.lesson_model.objects.prefetch_related('chapters').filter,
            chapters__pk=chapter_id
        )
        return lessons_of_chapter
    
    async def get_lesson_content(self, lesson_id: int):
        lesson_content = await self.lesson_model.objects.aget(pk=lesson_id)
        return lesson_content
    
    async def enroll_course(self, user: User, course_id: int, status: str = UserEnrollment.STATUS_ENROLLED):
        check_exist = await afilter(
            self.user_enrollment_model.objects.select_related('user', 'course').filter,
            user=user,
            course__pk=course_id
        )
        if check_exist.__len__() > 0:
            return {
                **check_exist[0].__dict__,
                'message': 'User already enrolled in this course'
            }
        
        user_enrollment = await self.user_enrollment_model.objects.acreate(
            user=user,
            course=await self.course_model.objects.aget(pk=course_id),
            status=status
        )
        return {
            **user_enrollment.__dict__,
            'message': 'User enrolled in course'
        }
    
    async def get_user_enrollments(self, user: User):
        user_enrollments = await afilter(
            self.user_enrollment_model.objects.select_related('user', 'course').filter,
            user=user
        )
        return [
            {
                'username': user_enrollment.user.username,
                'course_title': user_enrollment.course.name,
                'status': user_enrollment.status,
            }
            for user_enrollment in user_enrollments
        ]
    
    async def get_all_user_enrollments(self):
        user_enrollments = await alist_model(
            self.user_enrollment_model.objects.select_related('user', 'course').all
        )
        return [
            {
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

        
