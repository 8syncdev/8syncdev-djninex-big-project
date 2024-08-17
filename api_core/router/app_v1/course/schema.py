from ninja import (
    ModelSchema,
    Schema,
)
from .model import (
    UserEnrollment,
    Course
)

class CourseInputSchema(ModelSchema):
    class Meta:
        model = Course
        fields = (
            'name',
            'description',
            'img_url',
        )