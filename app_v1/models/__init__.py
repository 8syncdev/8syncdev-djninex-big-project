from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

# Mô hình User, kế thừa từ AbstractUser
class User(AbstractUser):
    phone = models.CharField(max_length=15, blank=True, null=True, db_index=True)  # Thêm db_index cho phone
    address = models.ManyToManyField('Address', blank=True)

    class Meta:
        indexes = [
            models.Index(fields=['username']),  # Thêm index cho trường username
            models.Index(fields=['email']),     # Thêm index cho trường email
        ]

class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip = models.CharField(max_length=10)
    country = models.CharField(max_length=100)

    class Meta:
        indexes = [
            models.Index(fields=['city', 'state']),  # Thêm index cho city và state
        ]

class Instructor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialty = models.CharField(max_length=100)
    bio = models.TextField()

class Course(models.Model):
    name = models.CharField(max_length=255)
    img_url = models.URLField(blank=True)
    price = models.FloatField()
    author = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    category = models.ManyToManyField('Category')
    chapters = models.ManyToManyField('Chapter', blank=True)
    tags = models.ManyToManyField('Tag', blank=True)

    class Meta:
        indexes = [
            models.Index(fields=['name']),  # Thêm index cho tên khóa học
            models.Index(fields=['price']),  # Thêm index cho giá khóa học
        ]

class Tag(models.Model):
    name = models.CharField(max_length=100)

class Review(models.Model):
    comment = models.TextField()
    rating = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    class Meta:
        indexes = [
            models.Index(fields=['rating']),  # Thêm index cho rating
        ]

class Lesson(models.Model):
    name = models.CharField(max_length=255)
    content = models.TextField()
    reviews = models.ManyToManyField(Review, blank=True)
    exercises = models.ManyToManyField('Exercise', blank=True)

class Chapter(models.Model):
    name = models.CharField(max_length=255)
    content = models.TextField()
    lessons = models.ManyToManyField(Lesson, blank=True)

class UserEnrollment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    audit = models.OneToOneField('Audit', on_delete=models.CASCADE)

    class Meta:
        indexes = [
            models.Index(fields=['user', 'course']),  # Thêm index cho user và course
        ]

class Exercise(models.Model):
    level = models.CharField(max_length=50)
    content = models.TextField()
    submissions = models.ManyToManyField('UserSubmission', blank=True)

class Submission(models.Model):
    code = models.TextField()
    grade = models.FloatField()
    audit = models.OneToOneField('Audit', on_delete=models.CASCADE)

class UserSubmission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    submission = models.ForeignKey(Submission, on_delete=models.CASCADE)

class Category(models.Model):
    name = models.CharField(max_length=100)

class Audit(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=100)
    updated_by = models.CharField(max_length=100)

class Payment(models.Model):
    amount = models.FloatField()
    date = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    courses = models.ManyToManyField(Course)

    class Meta:
        indexes = [
            models.Index(fields=['date']),  # Thêm index cho ngày thanh toán
        ]

class Notification(models.Model):
    message = models.TextField()
    date_sent = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Subscription(models.Model):
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    courses = models.ManyToManyField(Course)
    status = models.CharField(max_length=50)
    audit = models.OneToOneField(Audit, on_delete=models.CASCADE)

    class Meta:
        indexes = [
            models.Index(fields=['start_date', 'end_date']),  # Thêm index cho ngày bắt đầu và ngày kết thúc
        ]
