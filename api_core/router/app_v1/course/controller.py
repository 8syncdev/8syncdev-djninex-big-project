from api_core.common.restfull import *

from .schema import (
    CourseOutputSchema,
    ChaptersOfCourseOutputSchema,
    LessonsOfChapterOutputSchema,
    LessonContentOutputSchema,
    UserEnrollmentOutputSchema,
)

from .service import (
    CourseService,
)

from .model import (
    UserEnrollment,
)


@api_controller(
    prefix_or_class='/course',
    tags=['Course'],
)
class CourseController:

    def __init__(self, 
                 course_service: CourseService
                 ):
        self.course_service = course_service

    @route.get(
        path='',
        summary='Get all courses',
    )
    @paginate_dev()
    async def get_all(self, request):
        try:
            data = await self.course_service.get_courses()
            return list(map(CourseOutputSchema.from_orm, data))
        except Exception as e:
            return res_invalid(f"Failed to get courses, {e}")

    @route.get(
        path='/{course_id}/chapters',
        summary='Get chapters for a course',
    )
    @paginate_dev()
    async def get_chapters_of_course(self, request, course_id: int):
        try:
            data = await self.course_service.get_chapters_of_course(course_id)
            return list(map(ChaptersOfCourseOutputSchema.from_orm, data))
        except Exception as e:
            return res_invalid(f"Failed to get chapters, {e}")

    @route.get(
        path='/chapters/{chapter_id}/lessons',
        summary='Get lessons for a chapter',
        auth=AsyncJWTAuth(),
        permissions=[IsAuthenticated]
    )
    @paginate_dev()
    async def get_lessons_of_chapter(self, request, chapter_id: int):
        try:
            data = await self.course_service.get_lessons_of_chapter(chapter_id, request.user)
            if data.__len__() == 0:
                return ['No lessons']
            else:
                if data[0] == 'Expired':
                    return data
                elif data[0] == 'Not enrolled':
                    return data
            return list(map(LessonsOfChapterOutputSchema.from_orm, data))
        except Exception as e:
            return res_invalid(f"Failed to get lessons, {e}")
        
    @route.get(
        path='/lessons/{lesson_id}/content',
        summary='Get content for a lesson',
        auth=AsyncJWTAuth(),
        permissions=[IsAuthenticated]
    )
    async def get_lesson_content(self, request, lesson_id: int):
        try:
            data = await self.course_service.get_lesson_content(lesson_id)
            return res_valid(LessonContentOutputSchema.from_orm(data))
        except Exception as e:
            return res_invalid(f"Failed to get lesson content, {e}")
        
    @route.post(
        path='/enroll',
        summary='Enroll a course',
        auth=AsyncJWTAuth(),
        permissions=[IsAuthenticated]
    )
    async def enroll_course(self, request: Request, course_id: int, status: str = UserEnrollment.STATUS_ENROLLED):
        try:
            if request.user.is_superuser:
                data = await self.course_service.enroll_course(request.user, course_id, status)
            else:
                data = await self.course_service.enroll_course(request.user, course_id)
            return res_valid(UserEnrollmentOutputSchema.from_orm(data))
        except Exception as e:
            return res_invalid(f"Failed to enroll course, {e}")
        
    @route.get(
        path='/enrollments',
        summary='Get enrollments of user',
        auth=AsyncJWTAuth(),
    )
    @paginate_dev()
    async def get_user_enrollments(self, request):
        try:
            data = await self.course_service.get_user_enrollments(request.user)
            return data
        except Exception as e:
            return res_invalid(f"Failed to get user enrollments, {e}")
        
    @route.get(
        path='/enrollments/all',
        summary='Get all user enrollments',
        auth=AsyncJWTAuth(),
        permissions=[IsAdminUser]
    )
    @paginate_dev()
    async def get_all_user_enrollments(self, request):
        try:
            data = await self.course_service.get_all_user_enrollments()
            return data
        except Exception as e:
            return res_invalid(f"Failed to get all user enrollments, {e}")
        

    @route.delete(
        path='/enrollments/all',
        summary='Delete all user enrollments',
        auth=AsyncJWTAuth(),
        permissions=[IsAdminUser]
    )
    async def delete_all_user_enrollments(self, request):
        try:
            data = await self.course_service.delete_all_user_enrollments()
            return res_valid(data)
        except Exception as e:
            return res_invalid(f"Failed to delete all user enrollments, {e}")
    

