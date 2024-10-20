from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from users.models import User
from products.models import Category, Product
from orders.models import Order, OrderItem
from rest_framework_simplejwt.tokens import RefreshToken

class OrderProcessingTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        refresh = RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')

        self.category = Category.objects.create(name='Electronics')
        self.product1 = Product.objects.create(
            category=self.category,
            name='Smartphone',
            description='Latest smartphone model.',
            price=800.00,
            stock=50
        )
        self.product2 = Product.objects.create(
            category=self.category,
            name='Headphones',
            description='Noise-cancelling headphones.',
            price=200.00,
            stock=100
        )

    def test_create_order(self):
        url = reverse('order-list')  # Ensure 'order-list' is the correct route name
        data = {
            'items': [
                {'product_id': self.product1.id, 'quantity': 2},
                {'product_id': self.product2.id, 'quantity': 1},
            ]
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Order.objects.count(), 1)
        self.assertEqual(OrderItem.objects.count(), 2)
        order = Order.objects.get()
        self.assertEqual(order.items.count(), 2)
        self.assertEqual(order.user, self.user)
        # Verify stock reduction
        self.product1.refresh_from_db()
        self.product2.refresh_from_db()
        self.assertEqual(self.product1.stock, 48)
        self.assertEqual(self.product2.stock, 99)
