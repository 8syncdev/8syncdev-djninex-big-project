# from .user import User
# from .course import (
#     Course,
#     UserEnrollment
# )

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify

class ContentType(models.TextChoices):
    MD = 'md', 'Markdown'
    HTML = 'html', 'HTML'
    URL = 'url', 'URL'

class AbstractSluggedModel(models.Model):
    name = models.CharField(max_length=255)  # Không cần db_index
    slug = models.SlugField(max_length=255, unique=True, blank=True)  # Giữ db_index vì slug thường được truy vấn

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True

class AbstractContentModel(AbstractSluggedModel):
    
    content_type = models.CharField(max_length=50, choices=ContentType.choices, default=ContentType.MD)  # Không cần db_index
    content = models.JSONField(blank=True, null=True)  # Không cần db_index

    created_at = models.DateTimeField(auto_now_add=True, db_index=True)  # Giữ db_index
    updated_at = models.DateTimeField(auto_now=True, db_index=True)  # Giữ db_index

    class Meta:
        abstract = True

class User(AbstractUser):
    phone = models.CharField(max_length=15, blank=True, null=True)  # Không cần db_index

class Tag(AbstractSluggedModel):
    name = models.CharField(max_length=50, unique=True, db_index=True)  # Giữ db_index, vì tag có thể dùng trong tìm kiếm

class Category(AbstractSluggedModel):
    description = models.TextField()  # Không cần db_index

class Course(AbstractContentModel):
    # description = models.TextField()  # Không cần db_index
    tags = models.ManyToManyField(Tag, related_name='courses')  # Không cần db_index
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='courses', db_index=True)  # Giữ db_index, thường dùng để filter, join
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='courses', db_index=True)  # Giữ db_index
    img_url = models.URLField(blank=True, null=True)  # Không cần db_index
    price = models.DecimalField(max_digits=10, decimal_places=2, db_index=True)  # Giữ db_index, thường dùng để filter, sort

class Chapter(AbstractContentModel):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='chapters', db_index=True)  # Giữ db_index
    order = models.PositiveIntegerField(db_index=True)  # Giữ db_index, có thể dùng trong sắp xếp

    def __str__(self):
        return f'Chapter {self.order}: {self.name}'

    class Meta:
        unique_together = ('course', 'order')
        indexes = [
            models.Index(fields=['course', 'order']),
        ]

class Lesson(AbstractContentModel):
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, related_name='lessons', db_index=True)  # Giữ db_index
    order = models.PositiveIntegerField(db_index=True)  # Giữ db_index, có thể dùng trong sắp xếp

    def __str__(self):
        return f'Lesson {self.order}: {self.name}'

    class Meta:
        unique_together = ('chapter', 'order')
        indexes = [
            models.Index(fields=['chapter', 'order']),
        ]

class UserEnrollment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_enrollments', db_index=True)  # Giữ db_index
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='user_enrollments', db_index=True)  # Giữ db_index
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)  # Giữ db_index
    updated_at = models.DateTimeField(auto_now=True, db_index=True)  # Giữ db_index

    class Meta:
        unique_together = ('user', 'course')
        indexes = [
            models.Index(fields=['user', 'course']),
        ]

class AbstractReview(models.Model):
    # course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='reviews', db_index=True)  # Giữ db_index
    # lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='reviews', db_index=True)  # Giữ db_index
    rating = models.PositiveIntegerField(db_index=True)  # Giữ db_index, thường dùng để filter
    comment = models.TextField()  # Không cần db_index
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)  # Giữ db_index
    updated_at = models.DateTimeField(auto_now=True, db_index=True)  # Giữ db_index

    class Meta:
        abstract = True

class CourseReview(AbstractReview):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='course_reviews', db_index=True)  # Giữ db_index
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='reviews', db_index=True)  # Giữ db_index

    class Meta:
        unique_together = ('user', 'course')
        indexes = [
            models.Index(fields=['user', 'course']),
        ]

class LessonReview(AbstractReview):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='lesson_reviews', db_index=True)  # Giữ db_index
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='reviews', db_index=True)  # Giữ db_index

    class Meta:
        unique_together = ('user', 'lesson')
        indexes = [
            models.Index(fields=['user', 'lesson']),
        ]



# class Payment(models.Model):
#     class Status(models.TextChoices):
#         PENDING = 'pending', 'Pending'
#         COMPLETED = 'completed', 'Completed'
#         FAILED = 'failed', 'Failed'

#     user = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True)  # Giữ db_index
#     course = models.ForeignKey(Course, on_delete=models.CASCADE, db_index=True)  # Giữ db_index
#     amount = models.DecimalField(max_digits=10, decimal_places=2, db_index=True)  # Giữ db_index, thường dùng để filter
#     status = models.CharField(max_length=50, choices=Status.choices, default=Status.PENDING, db_index=True)  # Giữ db_index, thường dùng để filter
#     created_at = models.DateTimeField(auto_now_add=True, db_index=True)  # Giữ db_index
#     updated_at = models.DateTimeField(auto_now=True, db_index=True)  # Giữ db_index

#     class Meta:
#         indexes = [
#             models.Index(fields=['user', 'course']),
#         ]
