from ninja import ModelSchema, Schema, Field
from .model import Course, Chapter, Lesson, UserEnrollment
from .const import content_course

class CourseOutputSchema(ModelSchema):
    class Meta:
        model = Course
        fields = (
            'name',
            'img_url',
            'price',
            'description',
        )

class ChaptersOfCourseOutputSchema(ModelSchema):
    class Meta:
        model = Chapter
        fields = (
            'id',
            'name',
        )

class LessonsOfChapterOutputSchema(ModelSchema):
    class Meta:
        model = Lesson
        fields = (
            'id',
            'name',
            'is_trial'
        )

class LessonContentOutputSchema(ModelSchema):
    class Meta:
        model = Lesson
        fields = (
            'name',
            'url_video',
            'url_doc',
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


class CreateOrUpdateContentJsonCourseInputSchema(Schema):
    course_id: int = Field(gt=0)
    content_json: dict = content_course

class CreateOrUpdateContentJsonCourseOutputSchema(ModelSchema):
    class Meta:
        model = Course
        fields = (
            'content_json',
        )

class EnrollCourseInputSchema(Schema):
    course_id: int = Field(..., gt=0)
    status: str = 'enrolled'
    is_trial: bool = False


class GetCourseByIdOutputSchema(ModelSchema):

    class Meta:
        model = Course
        fields = (
            'name',
            'img_url',
            'description',
            'price',
            'content_json',
            'duration',
            # 'created_at',
            # 'updated_at',
        )

