import os
import django
import unittest
from django.test import TestCase
import json

# Set up Django settings before importing TestCase
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api_core.settings')
django.setup()

BASE_URL = '/v1/api'

def print_color(text, color_code):
    print(f"\033[{color_code}m{text}\033[0m")

# User data that will be available after running TestAppV1
CONST_USER = [
    {
        "username": "user1",
        "password": "123"
    },
    {
        "username": "admin",
        "password": "123"
    }
]

class TestAppV1(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user_token = None
        cls.admin_token = None

    def setUp(self):
        self.client.defaults['HTTP_AUTHORIZATION'] = ''

    def test_a_delete_all_data(self):
        # Test deleting all data
        response = self.client.get(f'{BASE_URL}/test-appv1/delete-all')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'message': 'Deleted all data successfully'})
        print_color('Deleted all data successfully', 32)

    def test_b_create_all_data(self):
        # Test creating all data
        response = self.client.get(f'{BASE_URL}/test-appv1/create-all-data')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'success': 'Done'})
        print_color('Created all data successfully', 32)

    def test_c_user_login(self):
        # Test user login functionality
        for user in CONST_USER:
            response = self.client.post(f'{BASE_URL}/token/pair', data=json.dumps(user), content_type='application/json')
            self.assertEqual(response.status_code, 200)
            data = response.json()
            self.assertIn('access', data)
            if user['username'] == 'user1':
                self.__class__.user_token = data['access']
            elif user['username'] == 'admin':
                self.__class__.admin_token = data['access']
        print_color('User login successful', 32)

    def test_d_get_courses(self):
        # Test retrieving courses
        response = self.client.get(f'{BASE_URL}/courses')
        self.assertEqual(response.status_code, 200)
        courses_data = response.json()
        self.assertIn('results', courses_data)
        self.assertIsInstance(courses_data['results'], list)
        self.assertGreater(len(courses_data['results']), 0)
        print_color('Get courses successful', 32)

    def test_e_enroll_course(self):
        # Test course enrollment
        self.client.defaults['HTTP_AUTHORIZATION'] = f'Bearer {self.__class__.user_token}'
        data = {
            "course_id": 1,
            "is_trial": False
        }
        response = self.client.post(f'{BASE_URL}/courses/enrollments/enroll', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        enrollment = response.json()
        self.assertIn('success', enrollment)
        self.assertTrue(enrollment['success'])
        self.assertIn('detail', enrollment)
        detail = enrollment['detail']
        self.assertIn('message', detail)
        self.assertEqual(detail['message'], 'User enrolled in course')
        self.assertEqual(detail['status'], 'enrolled')
        self.assertEqual(detail['course'], data['course_id'])
        self.assertIsNotNone(detail['user'])
        print_color('Course enrollment successful', 32)

    def test_f_create_payment(self):
        # Test payment creation
        self.client.defaults['HTTP_AUTHORIZATION'] = f'Bearer {self.__class__.user_token}'
        response = self.client.post(f'{BASE_URL}/payments/user', data=json.dumps({}), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        payment = response.json()
        self.assertIn('amount', payment)
        self.assertIn('status', payment)
        print_color('Payment creation successful', 32)

    def test_g_get_user_permissions(self):
        # Test retrieving user permissions
        self.client.defaults['HTTP_AUTHORIZATION'] = f'Bearer {self.__class__.admin_token}'
        response = self.client.get(f'{BASE_URL}/permissions/users')
        self.assertEqual(response.status_code, 200)
        permissions_data = response.json()
        self.assertIsInstance(permissions_data, dict)
        self.assertIn('results', permissions_data)
        self.assertIsInstance(permissions_data['results'], list)
        self.assertTrue(len(permissions_data['results']) > 0)
        for user_permissions in permissions_data['results']:
            self.assertIn('user', user_permissions)
            self.assertIn('permissions', user_permissions)
            self.assertIsInstance(user_permissions['permissions'], list)
        print_color('Get user permissions successful', 32)

class TestUser(TestCase):
    def setUp(self):
        self.client.defaults['HTTP_AUTHORIZATION'] = ''
        self.user_token = None
        self.admin_token = None

    def test_a_user_registration(self):
        # Test user registration
        data = {
            "username": "newuser",
            "password": "newpassword",
            "phone": "1234567890"
        }
        response = self.client.post(f'{BASE_URL}/users', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        user_data = response.json()
        self.assertIn('success', user_data)
        self.assertTrue(user_data['success'])
        self.assertIn('detail', user_data)
        detail = user_data['detail']
        self.assertIn('username', detail)
        self.assertEqual(detail['username'], 'newuser')
        self.assertIn('email', detail)
        self.assertIn('phone', detail)
        self.assertEqual(detail['phone'], '1234567890')
        self.assertIn('first_name', detail)
        self.assertIn('last_name', detail)
        print_color('User registration successful', 32)

    def test_b_user_login(self):
        # Test user login
        data = {
            "username": "user1",
            "password": "123"
        }
        response = self.client.post(f'{BASE_URL}/token/pair', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        login_data = response.json()
        self.assertIn('access', login_data)
        self.user_token = login_data['access']
        print_color('User login successful', 32)

    def test_c_update_user_info(self):
        # Test updating user information
        self.test_b_user_login()  # Ensure we have a user token
        self.client.defaults['HTTP_AUTHORIZATION'] = f'Bearer {self.user_token}'
        data = {
            "username": "updateduser",
            "password": "newpassword",
            "email": "updated@example.com",
            "first_name": "Updated",
            "last_name": "User"
        }
        response = self.client.patch(f'{BASE_URL}/users/me', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        updated_user = response.json()
        self.assertIn('success', updated_user)
        self.assertTrue(updated_user['success'])
        self.assertIn('detail', updated_user)
        detail = updated_user['detail']
        
        # Check if the response matches the expected fields
        self.assertIn('username', detail)
        self.assertIn('email', detail)
        self.assertIn('first_name', detail)
        self.assertIn('last_name', detail)
        
        # Verify the updated values
        self.assertEqual(detail['username'], "updateduser")
        self.assertEqual(detail['email'], "updated@example.com")
        self.assertEqual(detail['first_name'], "Updated")
        self.assertEqual(detail['last_name'], "User")
        
        # Note: We can't verify the password as it shouldn't be returned in the response
        
        # Verify that the response includes other expected fields
        self.assertIn('phone', detail)
        
        print_color('User information update successful', 32)

class TestCourse(TestCase):
    def setUp(self):
        self.client.defaults['HTTP_AUTHORIZATION'] = ''
        self.user_token = None

    def test_a_get_all_courses(self):
        # Test retrieving all courses
        response = self.client.get(f'{BASE_URL}/courses')
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIsInstance(data, dict)
        self.assertIn('count', data)
        self.assertIn('next', data)
        self.assertIn('previous', data)
        self.assertIn('results', data)
        self.assertIsInstance(data['results'], list)
        self.assertGreater(len(data['results']), 0)
        print_color('Get all courses successful', 32)

    def test_b_get_course_details(self):
        # Test retrieving course details
        course_id = 1  # Assuming course with ID 1 exists
        response = self.client.get(f'{BASE_URL}/courses/{course_id}')
        self.assertEqual(response.status_code, 200)
        course_details = response.json()
        self.assertIn('name', course_details)
        self.assertIn('description', course_details)
        print_color('Get course details successful', 32)

    def test_c_enroll_course(self):
        # Test course enrollment (requires user authentication)
        # First, login to get the user token
        login_data = {
            "username": "user1",
            "password": "123"
        }
        login_response = self.client.post(f'{BASE_URL}/token/pair', data=json.dumps(login_data), content_type='application/json')
        self.assertEqual(login_response.status_code, 200)
        self.user_token = login_response.json()['access']

        # Now enroll in a course
        self.client.defaults['HTTP_AUTHORIZATION'] = f'Bearer {self.user_token}'
        enroll_data = {
            "course_id": 1,
            "status": "enrolled",
            "is_trial": False
        }
        response = self.client.post(f'{BASE_URL}/courses/enrollments/enroll', data=json.dumps(enroll_data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        enrollment = response.json()
        self.assertIsInstance(enrollment, dict)
        self.assertIn('success', enrollment)
        self.assertTrue(enrollment['success'])
        self.assertIn('detail', enrollment)
        detail = enrollment['detail']
        self.assertIn('message', detail)
        self.assertIn('user', detail)
        self.assertIn('course', detail)
        self.assertIn('status', detail)
        self.assertEqual(detail['status'], 'enrolled')
        print_color('Course enrollment successful', 32)

class TestPayment(TestCase):
    def setUp(self):
        self.client.defaults['HTTP_AUTHORIZATION'] = ''
        self.user_token = None

    def test_a_create_payment(self):
        # Test creating a payment (requires user authentication)
        # First, login to get the user token
        login_data = {
            "username": "user1",
            "password": "123"
        }
        login_response = self.client.post(f'{BASE_URL}/token/pair', data=json.dumps(login_data), content_type='application/json')
        self.assertEqual(login_response.status_code, 200)
        self.user_token = login_response.json()['access']

        # Now create a payment
        self.client.defaults['HTTP_AUTHORIZATION'] = f'Bearer {self.user_token}'
        response = self.client.post(f'{BASE_URL}/payments/user', data=json.dumps({}), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        payment = response.json()
        self.assertIsInstance(payment, dict)
        self.assertIn('amount', payment)
        self.assertIn('status', payment)
        print_color('Payment creation successful', 32)

    def test_b_get_pending_payments(self):
        # Test retrieving pending payments for a user
        # Assuming we have the user token from the previous test
        self.test_a_create_payment()
        response = self.client.get(f'{BASE_URL}/payments/user/1/pending')  # Assuming user ID is 1
        self.assertEqual(response.status_code, 200)
        pending_payments = response.json()
        self.assertIsInstance(pending_payments, dict)
        
        # Check if the pending payments match the expected schema
        self.assertIn('count', pending_payments)
        self.assertIn('next', pending_payments)
        self.assertIn('previous', pending_payments)
        self.assertIn('results', pending_payments)
        self.assertIsInstance(pending_payments['results'], list)
        
        for payment in pending_payments['results']:
            self.assertIn('id', payment)
            self.assertIn('amount', payment)
            self.assertIn('status', payment)
            self.assertIn('date', payment)
            self.assertIn('user', payment)
            self.assertIn('message', payment)
            
            # Verify the status is pending
            self.assertEqual(payment['status'], 'pending')
        
        # Verify that the pending payments are for the correct user
        user_id = 1  # Assuming user ID is 1
        for payment in pending_payments['results']:
            self.assertEqual(payment['user'], user_id)
        
        print_color('Get pending payments successful', 32)

class TestPermission(TestCase):
    def setUp(self):
        self.client.defaults['HTTP_AUTHORIZATION'] = ''
        self.admin_token = None

    def test_a_get_user_permissions(self):
        # Test retrieving user permissions (requires admin authentication)
        # First, login as admin to get the token
        login_data = {
            "username": "admin",
            "password": "123"
        }
        login_response = self.client.post(f'{BASE_URL}/token/pair', data=json.dumps(login_data), content_type='application/json')
        self.assertEqual(login_response.status_code, 200)
        self.admin_token = login_response.json()['access']

        # Now get user permissions
        self.client.defaults['HTTP_AUTHORIZATION'] = f'Bearer {self.admin_token}'
        response = self.client.get(f'{BASE_URL}/permissions/users')
        self.assertEqual(response.status_code, 200)
        permissions = response.json()
        self.assertIsInstance(permissions, dict)
        
        # Check if the permissions match the expected schema
        self.assertIn('count', permissions)
        self.assertIn('next', permissions)
        self.assertIn('previous', permissions)
        self.assertIn('results', permissions)
        self.assertIsInstance(permissions['results'], list)
        
        for user_permission in permissions['results']:
            self.assertIn('user', user_permission)
            self.assertIn('permissions', user_permission)
            self.assertIsInstance(user_permission['permissions'], list)
        
        print_color('Get user permissions successful', 32)

if __name__ == '__main__':
    unittest.main()