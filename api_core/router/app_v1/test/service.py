from app_v1.models import *

def delete_all():
    """
    Function to delete all records from all models.
    """
    models = [
        User,
        Address,
        Instructor,
        Course,
        Review,
        Lesson,
        Chapter,
        UserEnrollment,
        Exercise,
        Submission,
        UserSubmission,
        Payment,
        Notification,
        Subscription
    ]

    for model in models:
        model.objects.all().delete()

    print("All records deleted.")