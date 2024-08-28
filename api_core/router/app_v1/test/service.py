import random
from django.utils import timezone
from faker import Faker
from app_v1.models import (
    User,
    Address,
    Instructor,
    Course,
    Tag,
    Review,
    Lesson,
    Chapter,
    UserEnrollment,
    Exercise,
    Submission,
    UserSubmission,
    Category,
    Audit,
    Payment,
    Notification,
    Subscription
)

def populate_database(records_per_model=1000, locale='en_US', models_to_populate=None, retries=3):
    """
    Function to populate the database with fake data.
    
    Parameters:
        records_per_model (int): Number of records to generate for each model.
        locale (str): Locale to use for generating data.
        models_to_populate (list): List of models to populate. If None, all models will be populated.
        retries (int): Number of retry attempts for handling Exception exceptions.
    """
    fake = Faker(locale)
    Faker.seed(0)  # For reproducible results

    models = models_to_populate or ['User', 'Address', 'Instructor', 'Course', 'Tag', 'Review', 
                                    'Lesson', 'Chapter', 'UserEnrollment', 'Exercise', 'Submission', 
                                    'UserSubmission', 'Category', 'Audit', 'Payment', 'Notification', 
                                    'Subscription']

    def create_users():
        for _ in range(records_per_model):
            attempt = 0
            while attempt < retries:
                try:
                    user = User.objects.create(
                        username=fake.unique.user_name(),
                        email=fake.unique.email(),
                        phone=fake.phone_number(),
                        first_name=fake.first_name(),
                        last_name=fake.last_name(),
                    )
                    user.set_password(fake.password())
                    user.save()
                    print('Created User')
                    break
                except Exception as e:
                    attempt += 1
                    print(f"Exception: {e}. Retrying {attempt}/{retries}...")
            else:
                print("Failed to create User after maximum retries. Skipping.")

    def create_addresses():
        for _ in range(records_per_model):
            attempt = 0
            while attempt < retries:
                try:
                    Address.objects.create(
                        street=fake.street_address(),
                        city=fake.city(),
                        state=fake.state(),
                        zip=random.randint(10000, 99999),
                        country=fake.current_country()
                    )
                    print('Created Address')
                    break
                except Exception as e:
                    attempt += 1
                    print(f"Exception: {e}. Retrying {attempt}/{retries}...")
            else:
                print("Failed to create Address after maximum retries. Skipping.")

    def create_instructors():
        users = list(User.objects.all())
        for _ in range(records_per_model):
            attempt = 0
            while attempt < retries:
                try:
                    random_user = random.choice(users)
                    Instructor.objects.create(
                        user=random_user,
                        specialty=fake.job(),
                        bio=fake.text(max_nb_chars=200)
                    )
                    print('Created Instructor')
                    break
                except Exception as e:
                    attempt += 1
                    print(f"Exception: {e}. Retrying {attempt}/{retries}...")
            else:
                print("Failed to create Instructor after maximum retries. Skipping.")

    def create_courses():
        instructors = list(Instructor.objects.all())
        categories = list(Category.objects.all())
        for _ in range(records_per_model):
            attempt = 0
            while attempt < retries:
                try:
                    course = Course.objects.create(
                        name=fake.catch_phrase(),
                        img_url=fake.image_url(),
                        price=random.uniform(10.0, 500.0),
                        author=random.choice(instructors)
                    )
                    course.categories.set(random.sample(categories, k=random.randint(1, len(categories))))
                    print('Created Course')
                    break
                except Exception as e:
                    attempt += 1
                    print(f"Exception: {e}. Retrying {attempt}/{retries}...")
            else:
                print("Failed to create Course after maximum retries. Skipping.")

    def create_tags():
        for _ in range(records_per_model):
            attempt = 0
            while attempt < retries:
                try:
                    Tag.objects.create(
                        name=fake.word()
                    )
                    print('Created Tag')
                    break
                except Exception as e:
                    attempt += 1
                    print(f"Exception: {e}. Retrying {attempt}/{retries}...")
            else:
                print("Failed to create Tag after maximum retries. Skipping.")

    def create_reviews():
        users = list(User.objects.all())
        courses = list(Course.objects.all())
        for _ in range(records_per_model):
            attempt = 0
            while attempt < retries:
                try:
                    user = random.choice(users)
                    user_enrollment = UserEnrollment.objects.create(
                        user=user,
                        course=random.choice(courses),
                        audit=Audit.objects.create(
                            created_at=fake.date_time_this_year(),
                            updated_at=fake.date_time_this_year(),
                            created_by=f'{user.first_name} {user.last_name}',
                            updated_by=f'{user.first_name} {user.last_name}'
                        )
                    )
                    Review.objects.create(
                        comment=fake.text(max_nb_chars=200),
                        rating=random.randint(1, 5),
                        enrollment=user_enrollment
                    )
                    print('Created Review')
                    break
                except Exception as e:
                    attempt += 1
                    print(f"Exception: {e}. Retrying {attempt}/{retries}...")
            else:
                print("Failed to create Review after maximum retries. Skipping.")

    def create_lessons():
        for _ in range(records_per_model):
            attempt = 0
            while attempt < retries:
                try:
                    Lesson.objects.create(
                        name=fake.sentence(nb_words=5),
                        content=fake.text(max_nb_chars=500)
                    )
                    print('Created Lesson')
                    break
                except Exception as e:
                    attempt += 1
                    print(f"Exception: {e}. Retrying {attempt}/{retries}...")
            else:
                print("Failed to create Lesson after maximum retries. Skipping.")

    def create_chapters():
        lessons = list(Lesson.objects.all())
        for _ in range(records_per_model):
            attempt = 0
            while attempt < retries:
                try:
                    chapter = Chapter.objects.create(
                        name=fake.sentence(nb_words=3),
                        content=fake.text(max_nb_chars=1000)
                    )
                    chapter.lessons.set(random.sample(lessons, k=random.randint(1, len(lessons))))
                    print('Created Chapter')
                    break
                except Exception as e:
                    attempt += 1
                    print(f"Exception: {e}. Retrying {attempt}/{retries}...")
            else:
                print("Failed to create Chapter after maximum retries. Skipping.")

    def create_user_enrollments():
        users = list(User.objects.all())
        courses = list(Course.objects.all())
        for _ in range(records_per_model):
            attempt = 0
            while attempt < retries:
                try:
                    UserEnrollment.objects.create(
                        user=random.choice(users),
                        course=random.choice(courses),
                        audit=Audit.objects.create(
                            created_at=fake.date_time_this_year(),
                            updated_at=fake.date_time_this_year(),
                            created_by=fake.name(),
                            updated_by=fake.name()
                        )
                    )
                    print('Created User Enrollment')
                    break
                except Exception as e:
                    attempt += 1
                    print(f"Exception: {e}. Retrying {attempt}/{retries}...")
            else:
                print("Failed to create User Enrollment after maximum retries. Skipping.")

    def create_exercises():
        for _ in range(records_per_model):
            attempt = 0
            while attempt < retries:
                try:
                    Exercise.objects.create(
                        level=fake.random_element(elements=('Easy', 'Medium', 'Hard')),
                        content=fake.text(max_nb_chars=200)
                    )
                    print('Created Exercise')
                    break
                except Exception as e:
                    attempt += 1
                    print(f"Exception: {e}. Retrying {attempt}/{retries}...")
            else:
                print("Failed to create Exercise after maximum retries. Skipping.")

    def create_submissions():
        audits = list(Audit.objects.all())
        for _ in range(records_per_model):
            attempt = 0
            while attempt < retries:
                try:
                    Submission.objects.create(
                        code=fake.sentence(nb_words=10),
                        grade=random.uniform(0, 100),
                        audit=random.choice(audits)
                    )
                    print('Created Submission')
                    break
                except Exception as e:
                    attempt += 1
                    print(f"Exception: {e}. Retrying {attempt}/{retries}...")
            else:
                print("Failed to create Submission after maximum retries. Skipping.")

    def create_user_submissions():
        users = list(User.objects.all())
        submissions = list(Submission.objects.all())
        exercises = list(Exercise.objects.all())
        for _ in range(records_per_model):
            attempt = 0
            while attempt < retries:
                try:
                    UserSubmission.objects.create(
                        user=random.choice(users),
                        submission=random.choice(submissions),
                        exercise=random.choice(exercises)
                    )
                    print('Created User Submission')
                    break
                except Exception as e:
                    attempt += 1
                    print(f"Exception: {e}. Retrying {attempt}/{retries}...")
            else:
                                print("Failed to create User Submission after maximum retries. Skipping.")

    def create_categories():
        for _ in range(records_per_model):
            attempt = 0
            while attempt < retries:
                try:
                    Category.objects.create(
                        name=fake.word()
                    )
                    print('Created Category')
                    break
                except Exception as e:
                    attempt += 1
                    print(f"Exception: {e}. Retrying {attempt}/{retries}...")
            else:
                print("Failed to create Category after maximum retries. Skipping.")

    def create_audits():
        for _ in range(records_per_model):
            attempt = 0
            while attempt < retries:
                try:
                    Audit.objects.create(
                        created_at=fake.date_time_this_year(),
                        updated_at=fake.date_time_this_year(),
                        created_by=fake.name(),
                        updated_by=fake.name()
                    )
                    print('Created Audit')
                    break
                except Exception as e:
                    attempt += 1
                    print(f"Exception: {e}. Retrying {attempt}/{retries}...")
            else:
                print("Failed to create Audit after maximum retries. Skipping.")

    def create_payments():
        users = list(User.objects.all())
        for _ in range(records_per_model):
            attempt = 0
            while attempt < retries:
                try:
                    Payment.objects.create(
                        amount=random.uniform(20.0, 1000.0),
                        date=fake.date_time_this_year(),
                        status=fake.random_element(elements=('Completed', 'Pending', 'Failed')),
                        user=random.choice(users)
                    )
                    print('Created Payment')
                    break
                except Exception as e:
                    attempt += 1
                    print(f"Exception: {e}. Retrying {attempt}/{retries}...")
            else:
                print("Failed to create Payment after maximum retries. Skipping.")

    def create_notifications():
        users = list(User.objects.all())
        for _ in range(records_per_model):
            attempt = 0
            while attempt < retries:
                try:
                    Notification.objects.create(
                        message=fake.sentence(nb_words=15),
                        date_sent=fake.date_time_this_year(),
                        user=random.choice(users)
                    )
                    print('Created Notification')
                    break
                except Exception as e:
                    attempt += 1
                    print(f"Exception: {e}. Retrying {attempt}/{retries}...")
            else:
                print("Failed to create Notification after maximum retries. Skipping.")

    def create_subscriptions():
        users = list(User.objects.all())
        courses = list(Course.objects.all())
        audits = list(Audit.objects.all())
        for _ in range(records_per_model):
            attempt = 0
            while attempt < retries:
                try:
                    subscription = Subscription.objects.create(
                        start_date=fake.date_time_this_year(),
                        end_date=fake.date_time_this_year(),
                        status=fake.random_element(elements=('Active', 'Cancelled', 'Expired')),
                        user=random.choice(users),
                        audit=random.choice(audits)
                    )
                    subscription.courses.set(random.sample(courses, k=random.randint(1, len(courses))))
                    print('Created Subscription')
                    break
                except Exception as e:
                    attempt += 1
                    print(f"Exception: {e}. Retrying {attempt}/{retries}...")
            else:
                print("Failed to create Subscription after maximum retries. Skipping.")

    # Call model-specific functions based on selection
    if 'User' in models:
        create_users()
    if 'Address' in models:
        create_addresses()
    if 'Instructor' in models:
        create_instructors()
    if 'Course' in models:
        create_courses()
    if 'Tag' in models:
        create_tags()
    if 'Review' in models:
        create_reviews()
    if 'Lesson' in models:
        create_lessons()
    if 'Chapter' in models:
        create_chapters()
    if 'UserEnrollment' in models:
        create_user_enrollments()
    if 'Exercise' in models:
        create_exercises()
    if 'Submission' in models:
        create_submissions()
    if 'UserSubmission' in models:
        create_user_submissions()
    if 'Category' in models:
        create_categories()
    if 'Audit' in models:
        create_audits()
    if 'Payment' in models:
        create_payments()
    if 'Notification' in models:
        create_notifications()
    if 'Subscription' in models:
        create_subscriptions()

    print("Database population complete.")


def delete_all():
    """
    Function to delete all records from all models.
    """
    models = [
        User,
        Address,
        Instructor,
        Course,
        Tag,
        Review,
        Lesson,
        Chapter,
        UserEnrollment,
        Exercise,
        Submission,
        UserSubmission,
        Category,
        Audit,
        Payment,
        Notification,
        Subscription
    ]

    for model in models:
        model.objects.all().delete()

    print("All records deleted.")

# Example usage
# populate_database(records_per_model=500, locale='en_US', models_to_populate=['User', 'Address', 'Instructor', 'Course'], retries=3)

