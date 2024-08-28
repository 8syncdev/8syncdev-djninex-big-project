from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

# User model, inheriting from Django's AbstractUser
class User(AbstractUser):
    phone = models.CharField(max_length=15, blank=True, null=True, db_index=True)
    address = models.ManyToManyField('Address', blank=True, related_name='users')
    
   
    class Meta:
        indexes = [
            models.Index(fields=['username']),
            models.Index(fields=['email']),
        ]

class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip = models.CharField(max_length=10)
    country = models.CharField(max_length=100)

    class Meta:
        indexes = [
            models.Index(fields=['city', 'state']),
        ]

class Instructor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='instructor_profile')
    specialty = models.CharField(max_length=100)
    bio = models.TextField()

class Course(models.Model):
    name = models.CharField(max_length=255)
    img_url = models.URLField(blank=True)
    price = models.FloatField()
    author = models.ForeignKey(Instructor, on_delete=models.CASCADE, related_name='courses')
    categories = models.ManyToManyField('Category', blank=True, related_name='courses')
    chapters = models.ManyToManyField('Chapter', blank=True, related_name='courses')
    tags = models.ManyToManyField('Tag', blank=True, related_name='courses')
    reviews = models.ManyToManyField('Review', blank=True, related_name='courses')

    class Meta:
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['price']),
        ]

class Tag(models.Model):
    name = models.CharField(max_length=100)

class Review(models.Model):
    comment = models.TextField()
    rating = models.IntegerField()
    enrollment = models.ForeignKey('UserEnrollment', on_delete=models.CASCADE, related_name='reviews')

    class Meta:
        indexes = [
            models.Index(fields=['rating']),
        ]

class Lesson(models.Model):
    name = models.CharField(max_length=255)
    content = models.TextField()
    exercises = models.ManyToManyField('Exercise', blank=True, related_name='lessons')

class Chapter(models.Model):
    name = models.CharField(max_length=255)
    content = models.TextField()
    lessons = models.ManyToManyField(Lesson, blank=True, related_name='chapters')

class UserEnrollment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='enrollments')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='enrollments')
    audit = models.OneToOneField('Audit', on_delete=models.CASCADE, related_name='enrollment')

    class Meta:
        indexes = [
            models.Index(fields=['user', 'course']),
        ]

class Exercise(models.Model):
    level = models.CharField(max_length=50)
    content = models.TextField()
    submissions = models.ManyToManyField('UserSubmission', blank=True, related_name='exercises')

class Submission(models.Model):
    code = models.TextField()
    grade = models.FloatField()
    audit = models.OneToOneField('Audit', on_delete=models.CASCADE, related_name='submission')

class UserSubmission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='submissions')
    submission = models.ForeignKey(Submission, on_delete=models.CASCADE, related_name='user_submissions')
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, related_name='user_submissions')

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
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='payments')
    courses = models.ManyToManyField(Course, related_name='payments')

    class Meta:
        indexes = [
            models.Index(fields=['date']),
        ]

class Notification(models.Model):
    message = models.TextField()
    date_sent = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')

class Subscription(models.Model):
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscriptions')
    courses = models.ManyToManyField(Course, related_name='subscriptions')
    status = models.CharField(max_length=50)
    audit = models.OneToOneField(Audit, on_delete=models.CASCADE, related_name='subscription')

    class Meta:
        indexes = [
            models.Index(fields=['start_date', 'end_date']),
        ]
