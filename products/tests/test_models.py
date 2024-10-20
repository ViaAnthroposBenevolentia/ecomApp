from django.test import TestCase
from products.models import Category, Product

class ProductModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Electronics')
        self.product = Product.objects.create(
            category=self.category,
            name='Laptop',
            description='High-end gaming laptop',
            price=1500.00,
            stock=10
        )

    def test_product_creation(self):
        self.assertEqual(self.product.name, 'Laptop')
        self.assertEqual(self.product.category.name, 'Electronics')
        self.assertEqual(self.product.price, 1500.00)
        self.assertEqual(self.product.stock, 10)
