from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from users.models import User
from products.models import Category, Product
from rest_framework_simplejwt.tokens import RefreshToken

class ProductAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        refresh = RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')

        self.category = Category.objects.create(name='Books')
        self.product_data = {
            'name': 'Django for Beginners',
            'description': 'A comprehensive guide to Django.',
            'price': '30.00',
            'stock': 100,
            'category_id': self.category.id
        }

    def test_create_product(self):
        url = reverse('product-list')  # Ensure 'product-list' is the correct route name
        response = self.client.post(url, self.product_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 1)
        self.assertEqual(Product.objects.get().name, 'Django for Beginners')
