import random
from django.utils import timezone
from app_v1.models import *

def populate_database(records_per_model=1000, locale='en_US', models_to_populate=None, retries=3):
    """
    Function to populate the database with fake data.
    
    Parameters:
        records_per_model (int): Number of records to generate for each model.
        locale (str): Locale to use for generating data.
        models_to_populate (list): List of models to populate. If None, all models will be populated.
        retries (int): Number of retry attempts for handling Exception exceptions.
    """
    random.seed(0)  # For reproducible results

    models = models_to_populate or ['User', 'Address', 'Instructor', 'Course', 'Review', 
                                    'Lesson', 'Chapter', 'UserEnrollment', 'Exercise', 'Submission', 
                                    'UserSubmission', 'Category', 'Payment', 'Notification', 
                                    'Subscription']

    def create_users():
        for _ in range(records_per_model):
            attempt = 0
            while attempt < retries:
                try:
                    user = User.objects.create(
                        username=f"user_{random.randint(1, 1000000)}",
                        email=f"user_{random.randint(1, 1000000)}@example.com",
                        phone=f"{random.randint(100, 999)}-{random.randint(100, 999)}-{random.randint(1000, 9999)}",
                        first_name=f"FirstName{random.randint(1, 1000)}",
                        last_name=f"LastName{random.randint(1, 1000)}",
                    )
                    user.set_password(f"password{random.randint(1, 1000)}")
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
                        street=f"{random.randint(1, 999)} Street {random.randint(1, 100)}",
                        city=f"City{random.randint(1, 100)}",
                        state=f"State{random.randint(1, 50)}",
                        zip=random.randint(10000, 99999),
                        country=f"Country{random.randint(1, 50)}"
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
                        specialty=f"Specialty{random.randint(1, 100)}",
                        bio=f"Bio text for instructor {random.randint(1, 1000)}"
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
                        name=f"Course {random.randint(1, 1000)}",
                        img_url=f"https://example.com/image{random.randint(1, 1000)}.jpg",
                        price=round(random.uniform(10.0, 500.0), 2),
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

    def create_reviews():
        enrollments = list(UserEnrollment.objects.all())
        for _ in range(records_per_model):
            attempt = 0
            while attempt < retries:
                try:
                    Review.objects.create(
                        comment=f"Review comment {random.randint(1, 1000)}",
                        rating=random.randint(1, 5),
                        user_enrollment=random.choice(enrollments)
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
                        name=f"Lesson {random.randint(1, 1000)}",
                        content=f"Content for lesson {random.randint(1, 1000)}"
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
                        name=f"Chapter {random.randint(1, 1000)}",
                        content=f"Content for chapter {random.randint(1, 1000)}"
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
                        status=random.choice(['enrolled', 'completed', 'cancelled', 'pending'])
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
                        level=random.choice(['beginner', 'intermediate', 'advanced']),
                        content=f"Exercise content {random.randint(1, 1000)}"
                    )
                    print('Created Exercise')
                    break
                except Exception as e:
                    attempt += 1
                    print(f"Exception: {e}. Retrying {attempt}/{retries}...")
            else:
                print("Failed to create Exercise after maximum retries. Skipping.")

    def create_submissions():
        for _ in range(records_per_model):
            attempt = 0
            while attempt < retries:
                try:
                    Submission.objects.create(
                        code=f"Code submission {random.randint(1, 1000)}",
                        grade=round(random.uniform(0, 100), 2)
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
                        name=f"Category {random.randint(1, 1000)}"
                    )
                    print('Created Category')
                    break
                except Exception as e:
                    attempt += 1
                    print(f"Exception: {e}. Retrying {attempt}/{retries}...")
            else:
                print("Failed to create Category after maximum retries. Skipping.")

    def create_payments():
        users = list(User.objects.all())
        for _ in range(records_per_model):
            attempt = 0
            while attempt < retries:
                try:
                    Payment.objects.create(
                        amount=round(random.uniform(20.0, 1000.0), 2),
                        date=timezone.now() - timezone.timedelta(days=random.randint(0, 365)),
                        status=random.choice(['completed', 'pending', 'failed']),
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
                        message=f"Notification message {random.randint(1, 1000)}",
                        date_sent=timezone.now() - timezone.timedelta(days=random.randint(0, 30)),
                        user=random.choice(users),
                        notification_type=random.choice(['info', 'warning', 'error'])
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
        for _ in range(records_per_model):
            attempt = 0
            while attempt < retries:
                try:
                    subscription = Subscription.objects.create(
                        start_date=timezone.now() - timezone.timedelta(days=random.randint(0, 365)),
                        end_date=timezone.now() + timezone.timedelta(days=random.randint(0, 365)),
                        status=random.choice(['active', 'inactive', 'expired', 'pending', 'cancelled']),
                        user=random.choice(users)
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
        Review,
        Lesson,
        Chapter,
        UserEnrollment,
        Exercise,
        Submission,
        UserSubmission,
        Category,
        Payment,
        Notification,
        Subscription
    ]

    for model in models:
        model.objects.all().delete()

    print("All records deleted.")


def populate_data():
    # Create User instances with real data
    users = [
        User.objects.create_user(username="john_doe", email="john.doe@example.com", password="password123", phone="123-456-7890"),
        User.objects.create_user(username="jane_smith", email="jane.smith@example.com", password="password123", phone="123-456-7891"),
        User.objects.create_user(username="alice_jones", email="alice.jones@example.com", password="password123", phone="123-456-7892"),
        User.objects.create_user(username="bob_brown", email="bob.brown@example.com", password="password123", phone="123-456-7893"),
        User.objects.create_user(username="charlie_black", email="charlie.black@example.com", password="password123", phone="123-456-7894")
    ]
    
    # Create Address instances with real data
    addresses = [
        Address.objects.create(street="123 Elm St", city="New York", state="NY", zip="10001", country="USA"),
        Address.objects.create(street="456 Oak St", city="Los Angeles", state="CA", zip="90001", country="USA"),
        Address.objects.create(street="789 Pine St", city="Chicago", state="IL", zip="60601", country="USA"),
        Address.objects.create(street="101 Maple St", city="Houston", state="TX", zip="77001", country="USA"),
        Address.objects.create(street="202 Birch St", city="Phoenix", state="AZ", zip="85001", country="USA")
    ]

    # Associate users with addresses
    for user, address in zip(users, addresses):
        user.addresses.add(address)
        user.save()

    # Create Instructor instances with real data
    instructors = [
        Instructor.objects.create(user=users[0], specialty="Mathematics", bio="Experienced in teaching high school and college-level math."),
        Instructor.objects.create(user=users[1], specialty="Physics", bio="Physics instructor with a passion for quantum mechanics."),
        Instructor.objects.create(user=users[2], specialty="Computer Science", bio="Software developer with a love for teaching programming."),
        Instructor.objects.create(user=users[3], specialty="History", bio="Historian with a focus on ancient civilizations."),
        Instructor.objects.create(user=users[4], specialty="Literature", bio="Literature professor specializing in 19th-century novels.")
    ]

    # Create Category instances
    categories = [
        Category.objects.create(name="Science"),
        Category.objects.create(name="Mathematics"),
        Category.objects.create(name="Computer Science"),
        Category.objects.create(name="History"),
        Category.objects.create(name="Literature")
    ]

    # Create Chapter instances with real data
    chapters = [
        Chapter.objects.create(name="Introduction to Algebra", content="This chapter covers the basics of algebra."),
        Chapter.objects.create(name="Quantum Mechanics Fundamentals", content="Introduction to the principles of quantum mechanics."),
        Chapter.objects.create(name="Python Programming Basics", content="Learn the basics of Python programming."),
        Chapter.objects.create(name="Ancient Egyptian History", content="Explore the history of ancient Egypt."),
        Chapter.objects.create(name="Victorian Literature", content="An overview of literature during the Victorian era.")
    ]

    # Create Course instances with real data
    courses = [
        Course.objects.create(name="Algebra 101", img_url="", price=50.0, author=instructors[0]),
        Course.objects.create(name="Quantum Physics", img_url="", price=75.0, author=instructors[1]),
        Course.objects.create(name="Introduction to Python", img_url="", price=40.0, author=instructors[2]),
        Course.objects.create(name="Ancient Civilizations", img_url="", price=60.0, author=instructors[3]),
        Course.objects.create(name="Classic Literature", img_url="", price=55.0, author=instructors[4])
    ]

    # Associate courses with categories and chapters
    for course, category, chapter in zip(courses, categories, chapters):
        course.categories.add(category)
        course.chapters.add(chapter)
        course.save()

    # Create Lesson instances
    lessons = [
        Lesson.objects.create(name="Lesson 1: Algebraic Expressions", content="Learn how to simplify algebraic expressions."),
        Lesson.objects.create(name="Lesson 1: Wave-Particle Duality", content="Understanding the dual nature of light."),
        Lesson.objects.create(name="Lesson 1: Variables and Data Types", content="Introduction to Python variables and data types."),
        Lesson.objects.create(name="Lesson 1: The Pyramids", content="Explore the history of the pyramids in Egypt."),
        Lesson.objects.create(name="Lesson 1: Gothic Novels", content="Analysis of Gothic literature in the 19th century.")
    ]

    # Associate lessons with chapters
    for chapter, lesson in zip(chapters, lessons):
        chapter.lessons.add(lesson)
        chapter.save()

    # Create Exercise instances
    exercises = [
        Exercise.objects.create(level="beginner", content="Solve the given algebraic equations.", name="Algebraic Equations"),
        Exercise.objects.create(level="intermediate", content="Calculate the energy levels in a quantum well.", name="Quantum Well Energy Levels"),
        Exercise.objects.create(level="beginner", content="Write a Python program to calculate factorial.", name="Factorial Program"),
        Exercise.objects.create(level="advanced", content="Analyze the political structure of Ancient Egypt.", name="Political Structure of Ancient Egypt"),
        Exercise.objects.create(level="intermediate", content="Compare the themes in 'Pride and Prejudice' and 'Wuthering Heights'.", name="Comparative Analysis of Novels")
    ]

    # Associate exercises with lessons
    for lesson, exercise in zip(lessons, exercises):
        lesson.exercises.add(exercise)
        lesson.save()

    # Create Submission instances
    submissions = [
        Submission.objects.create(code="print('Hello, world!')", grade=95.0),
        Submission.objects.create(code="x = 5 + 10", grade=88.0),
        Submission.objects.create(code="def factorial(n): return 1 if n == 0 else n * factorial(n-1)", grade=92.0),
        Submission.objects.create(code="class Car: pass", grade=85.0),
        Submission.objects.create(code="for i in range(5): print(i)", grade=90.0)
    ]

    # Create UserSubmission instances
    user_submissions = [
        UserSubmission.objects.create(user=users[0], submission=submissions[0], exercise=exercises[0]),
        UserSubmission.objects.create(user=users[1], submission=submissions[1], exercise=exercises[1]),
        UserSubmission.objects.create(user=users[2], submission=submissions[2], exercise=exercises[2]),
        UserSubmission.objects.create(user=users[3], submission=submissions[3], exercise=exercises[3]),
        UserSubmission.objects.create(user=users[4], submission=submissions[4], exercise=exercises[4])
    ]

    # Create UserEnrollment instances
    enrollments = [
        UserEnrollment.objects.create(user=users[0], course=courses[0], status="enrolled"),
        UserEnrollment.objects.create(user=users[1], course=courses[1], status="completed"),
        UserEnrollment.objects.create(user=users[2], course=courses[2], status="pending"),
        UserEnrollment.objects.create(user=users[3], course=courses[3], status="cancelled"),
        UserEnrollment.objects.create(user=users[4], course=courses[4], status="enrolled")
    ]

    # Create Review instances
    reviews = [
        Review.objects.create(comment="Great course on algebra!", rating=5, user_enrollment=enrollments[0]),
        Review.objects.create(comment="Quantum physics is tough, but this course helped a lot.", rating=4, user_enrollment=enrollments[1]),
        Review.objects.create(comment="Loved learning Python with real-world examples.", rating=5, user_enrollment=enrollments[2]),
        Review.objects.create(comment="Very informative course on ancient civilizations.", rating=4, user_enrollment=enrollments[3]),
        Review.objects.create(comment="A deep dive into classic literature, enjoyed it thoroughly.", rating=5, user_enrollment=enrollments[4])
    ]

    # Create Notification instances
    notifications = [
        Notification.objects.create(user=users[0], message="Welcome to Algebra 101!", notification_type="info", date_sent=timezone.now()),
        Notification.objects.create(user=users[1], message="New content available in Quantum Physics.", notification_type="info", date_sent=timezone.now()),
        Notification.objects.create(user=users[2], message="Your Python assignment has been graded.", notification_type="info", date_sent=timezone.now()),
        Notification.objects.create(user=users[3], message="New discussion topic in Ancient Civilizations.", notification_type="info", date_sent=timezone.now()),
        Notification.objects.create(user=users[4], message="Upcoming quiz in Classic Literature.", notification_type="warning", date_sent=timezone.now())
    ]

    # Create Subscription instances
    subscriptions = [
        Subscription.objects.create(user=users[0], start_date=timezone.now(), end_date=timezone.now() + timezone.timedelta(days=30), status="active"),
        Subscription.objects.create(user=users[1], start_date=timezone.now(), end_date=timezone.now() + timezone.timedelta(days=30), status="active"),
        Subscription.objects.create(user=users[2], start_date=timezone.now(), end_date=timezone.now() + timezone.timedelta(days=30), status="active"),
        Subscription.objects.create(user=users[3], start_date=timezone.now(), end_date=timezone.now() + timezone.timedelta(days=30), status="active"),
        Subscription.objects.create(user=users[4], start_date=timezone.now(), end_date=timezone.now() + timezone.timedelta(days=30), status="active")
    ]

    # Create Payment instances
    payments = [
        Payment.objects.create(user=users[0], amount=50.0, date=timezone.now(), status="completed"),
        Payment.objects.create(user=users[1], amount=75.0, date=timezone.now(), status="completed"),
        Payment.objects.create(user=users[2], amount=40.0, date=timezone.now(), status="completed"),
        Payment.objects.create(user=users[3], amount=60.0, date=timezone.now(), status="completed"),
        Payment.objects.create(user=users[4], amount=55.0, date=timezone.now(), status="completed")
    ]

    print("Data population completed successfully!")

