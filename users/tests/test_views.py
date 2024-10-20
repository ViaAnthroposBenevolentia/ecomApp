from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from users.models import User

class UserRegistrationTest(APITestCase):
    def test_user_registration(self):
        url = reverse('user-list')  # Ensure 'user-list' is the correct route name
        data = {
            'username': 'newuser',
            'password': 'newpass123',
            'password2': 'newpass123',
            'email': 'newuser@example.com',
            'first_name': 'New',
            'last_name': 'User'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().username, 'newuser')
