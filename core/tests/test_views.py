from django.test import TestCase, Client
from django.urls import reverse
from .models import User

class SignupViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.signup_url = reverse('signup')
        self.user_data = {
            'username': 'testuser',
            'password': 'testpassword',
            'email': 'test@example.com',
            'first_name': 'Test',
            'last_name': 'User',
            'avg': '3',
            'collage': 'testcollage'
        }

    def test_signup_view(self):
        response = self.client.post(self.signup_url, self.user_data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/profile/')

        user = User.objects.get(username='testuser')
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.email, 'test@example.com')
        self.assertEqual(user.first_name, 'Test')
        self.assertEqual(user.last_name, 'User')
        self.assertEqual(user.avg, '3')
        self.assertEqual(user.collage, 'testcollage')
