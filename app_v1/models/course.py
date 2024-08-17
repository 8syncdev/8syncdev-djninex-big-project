from django.db import models
from app_v1.models.user import User


class UserEnrollment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey('Course', on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.username} enrolled in {self.course.name}'


class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    tags = models.JSONField(default=list)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    users = models.ManyToManyField(
        User, 
        through=UserEnrollment, related_name='courses', 
    )
    img_url = models.URLField(max_length=200, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name