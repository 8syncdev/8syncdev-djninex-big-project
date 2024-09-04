from ninja import ModelSchema
from .model import Course, Chapter, Lesson, UserEnrollment

class CourseOutputSchema(ModelSchema):
    class Meta:
        model = Course
        fields = (
            'name',
            'img_url',
            'price',
            'description',
            'created_at',
            'updated_at',
        )

class ChaptersOfCourseOutputSchema(ModelSchema):
    class Meta:
        model = Chapter
        fields = (
            'name',
            'id',
        )

class LessonsOfChapterOutputSchema(ModelSchema):
    class Meta:
        model = Lesson
        fields = (
            'name',
            'id',
        )

class LessonContentOutputSchema(ModelSchema):
    class Meta:
        model = Lesson
        fields = (
            'content',
        )


class UserEnrollmentOutputSchema(ModelSchema):
    message: str
    class Meta:
        model = UserEnrollment
        fields = (
            'user',
            'course',
            'status',
        )

