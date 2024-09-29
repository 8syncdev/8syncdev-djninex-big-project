from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


# User model, inheriting from Django's AbstractUser
class User(AbstractUser):
    phone = models.CharField(max_length=15, blank=True, null=True, db_index=True, unique=True)
    addresses = models.ManyToManyField('Address', blank=True, related_name='users')

    class Meta:
        indexes = [
            models.Index(fields=['username']),
            models.Index(fields=['email']),
        ]

    def __str__(self):
        return self.username


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

    def __str__(self):
        return f"{self.street}, {self.city}, {self.state}, {self.country}"


class Instructor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='instructor_profile')
    specialty = models.CharField(max_length=100)
    bio = models.TextField()

    def __str__(self):
        return f"Instructor: {self.user.username} - Specialty: {self.specialty}"


class Course(models.Model):
    name = models.CharField(max_length=255)
    img_url = models.URLField(blank=True)
    price = models.FloatField()
    description = models.TextField(null=True, blank=True)
    content_json = models.JSONField(null=True, blank=True)
    duration = models.FloatField(null=True, blank=True)

    author = models.ForeignKey(Instructor, on_delete=models.CASCADE, related_name='courses')
    categories = ArrayField(models.CharField(max_length=100), blank=True, null=True)
    chapters = models.ManyToManyField('Chapter', blank=True, related_name='courses')
    voucher = models.OneToOneField('Voucher', null=True, blank=True, on_delete=models.SET_NULL, related_name='course')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['price']),
        ]

    def __str__(self):
        return self.name


class Voucher(models.Model):
    code = models.CharField(max_length=50, unique=True)
    discount = models.FloatField()
    expiration_date = models.DateTimeField()

    def __str__(self):
        return self.code


class Review(models.Model):
    comment = models.TextField()
    rating = models.IntegerField(choices=[
        (1, '1 - Poor'),
        (2, '2 - Fair'),
        (3, '3 - Good'),
        (4, '4 - Very Good'),
        (5, '5 - Excellent'),
    ])
    user_enrollment = models.ForeignKey('UserEnrollment', on_delete=models.CASCADE, related_name='reviews')

    def __str__(self):
        return f"Review by {self.user_enrollment.user.username} - Rating: {self.rating}"


class Lesson(models.Model):
    name = models.CharField(max_length=255)
    content = models.TextField()
    url_doc = models.URLField(max_length=500, null=True, blank=True)
    url_video = models.URLField(max_length=500,null=True, blank=True)
    is_trial = models.BooleanField(default=False)

    reviews = models.ManyToManyField(Review, blank=True, related_name='lessons')
    exercises = models.ManyToManyField('Exercise', blank=True, related_name='lessons')

    def __str__(self):
        return self.name


class Chapter(models.Model):
    name = models.CharField(max_length=255)
    content = models.TextField()
    lessons = models.ManyToManyField(Lesson, blank=True, related_name='chapters')

    def __str__(self):
        return self.name


class UserEnrollment(models.Model):
    EXPIRATION_DAYS = 30
    EXPIRATION_DAYS_TRIAL = 7
    EXPIRATION_TEST_MINUTES = 2

    STATUS_EXPIRED = 'expired'
    STATUS_CANCELLED = 'cancelled'
    STATUS_ENROLLED = 'enrolled'
    STATUS_PENDING = 'pending'
    STATUS_COMPLETED = 'completed'
    STATUS_TRIAL = 'trial'

    ENROLLMENT_STATUS_CHOICES = [
        (STATUS_ENROLLED, 'Enrolled'),
        (STATUS_COMPLETED, 'Completed'),
        (STATUS_TRIAL, 'Trial'),
        (STATUS_CANCELLED, 'Cancelled'),
        (STATUS_PENDING, 'Pending'),
        (STATUS_EXPIRED, 'Expired')
    ]

    status = models.CharField(max_length=50, choices=ENROLLMENT_STATUS_CHOICES, default=STATUS_PENDING)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    expiration_date = models.DateTimeField(default=timezone.now() + timezone.timedelta(minutes=EXPIRATION_TEST_MINUTES))
    is_check_expiration = models.BooleanField(default=False)

    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='enrollments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='enrollments')

    class Meta:
        indexes = [
            models.Index(fields=['user', 'course']),
        ]

    def __str__(self):
        return f"Enrollment: {self.user.username} in {self.course.name} - Status: {self.status}"


class Exercise(models.Model):
    name = models.CharField(max_length=255)
    level = models.CharField(max_length=50, choices=[
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    ])
    content = models.TextField()

    def __str__(self):
        return self.name


class Submission(models.Model):
    code = models.TextField()
    grade = models.FloatField()

    def __str__(self):
        return f"Submission with Grade: {self.grade}"


class UserSubmission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='submissions')
    submissions = models.ManyToManyField(Submission, related_name='user_submissions')
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, related_name='user_submissions')

    def __str__(self):
        return f"Submission by {self.user.username} for {self.exercise.name}"


class CategoryChoice(models.TextChoices):
    PYTHON = 'python', 'Python'
    WEB_FRAMEWORKS = 'web_frameworks', 'Web Frameworks'
    FRONTEND = 'frontend', 'Frontend'
    BACKEND = 'backend', 'Backend'
    PROGRAMMING_LANGUAGES = 'programming_languages', 'Programming Languages'
    DATABASE = 'database', 'Database'
    SOFTWARE_ENGINEERING = 'software_engineering', 'Software Engineering'
    DEVOPS = 'devops', 'DevOps'
    MOBILE_DEVELOPMENT = 'mobile_development', 'Mobile Development'
    TESTING = 'testing', 'Testing'


class Payment(models.Model):
    STATUS_PENDING = 'pending'
    STATUS_COMPLETED = 'completed'
    STATUS_FAILED = 'failed'

    PAYMENT_STATUS_CHOICES = [
        (STATUS_PENDING, 'Pending'),
        (STATUS_COMPLETED, 'Completed'),
        (STATUS_FAILED, 'Failed'),
    ]

    amount = models.FloatField()
    date = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=50, choices=PAYMENT_STATUS_CHOICES, default=STATUS_PENDING)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='payments')
    message = models.JSONField(null=True, blank=True)

    def __str__(self):
        return f"Payment of {self.amount} by {self.user.username} - Status: {self.status}"


class Notification(models.Model):
    TYPE_INFO = 'info'
    TYPE_WARNING = 'warning'
    TYPE_ERROR = 'error'

    NOTIFICATION_TYPE_CHOICES = [
        (TYPE_INFO, 'Info'),
        (TYPE_WARNING, 'Warning'),
        (TYPE_ERROR, 'Error'),
    ]

    message = models.TextField()
    date_sent = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    notification_type = models.CharField(max_length=50, choices=NOTIFICATION_TYPE_CHOICES, default=TYPE_INFO)

    def __str__(self):
        return f"Notification for {self.user.username} - Type: {self.notification_type}"


class Subscription(models.Model):
    STATUS_ACTIVE = 'active'
    STATUS_INACTIVE = 'inactive'
    STATUS_EXPIRED = 'expired'
    STATUS_PENDING = 'pending'
    STATUS_CANCELLED = 'cancelled'

    SUBSCRIPTION_STATUS_CHOICES = [
        (STATUS_ACTIVE, 'Active'),
        (STATUS_INACTIVE, 'Inactive'),
        (STATUS_EXPIRED, 'Expired'),
        (STATUS_PENDING, 'Pending'),
        (STATUS_CANCELLED, 'Cancelled'),
    ]

    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscriptions')
    status = models.CharField(max_length=50, choices=SUBSCRIPTION_STATUS_CHOICES, default=STATUS_ACTIVE)
    courses = models.ManyToManyField(Course, related_name='subscriptions')

    class Meta:
        indexes = [
            models.Index(fields=['start_date', 'end_date']),
        ]

    def __str__(self):
        return f"Subscription for {self.user.username} - Status: {self.status}"
