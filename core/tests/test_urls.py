from django.test import TestCase, Client
from django.urls import reverse
from .models import User

class UrlTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_signup_url(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)

    def test_login_url(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

    def test_logout_url(self):
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)

    def test_add_course_url(self):
        response = self.client.get(reverse('add-course'))
        self.assertEqual(response.status_code, 200)

    def test_all_courses_url(self):
        response = self.client.get(reverse('all-courses'))
        self.assertEqual(response.status_code, 200)

    def test_add_worker_url(self):
        response = self.client.get(reverse('add-worker'))
        self.assertEqual(response.status_code, 200)

    def test_all_workers_url(self):
        response = self.client.get(reverse('all-workers'))
        self.assertEqual(response.status_code, 200)

    def test_add_student_url(self):
        response = self.client.get(reverse('add-student'))
        self.assertEqual(response.status_code, 200)

    def test_all_students_url(self):
        response = self.client.get(reverse('all-students'))
        self.assertEqual(response.status_code, 200)

    def test_profile_url(self):
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 302)

    def test_account_settings_url(self):
        response = self.client.get(reverse('account-settings'))
        self.assertEqual(response.status_code, 302)

    def test_delete_user_url(self):
        response = self.client.get(reverse('delete_account',args=[1]))
        self.assertEqual(response.status_code, 302)

    def test_message_url(self):
        response = self.client.get(reverse('message'))
        self.assertEqual(response.status_code, 200)

    def test_add_message_url(self):
        response = self.client.get(reverse('add-message'))
        self.assertEqual(response.status_code, 200)
