from rest_framework import serializers
from .models import Category, Product

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']
        read_only_fields = ['id']

class ProductSerializer(serializers.ModelSerializer):
    """
    Serializer for the Product model.
    """
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), source='category', write_only=True
    )
    image = serializers.ImageField(required=False, allow_null=True)

    class Meta:
        model = Product
        fields = [
            'id', 'name', 'description', 'price', 'stock', 
            'category', 'category_id', 'image', 
            'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']
        extra_kwargs = {
            'name': {'help_text': 'Name of the product'},
            'price': {'help_text': 'Price of the product in USD'},
            'stock': {'help_text': 'Available stock quantity'},
            'image': {'help_text': 'Product image (optional)'},
        }
