from rest_framework import viewsets, permissions, filters
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer
from django_filters.rest_framework import DjangoFilterBackend
from django.core.cache import cache
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.select_related('category').all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend,
        filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category', 'price']
    search_fields = ['name', 'description']
    ordering_fields = ['price', 'created_at']
    ordering = ['created_at']  # Default ordering


    @swagger_auto_schema(
        operation_description="Create a new product.",
        request_body=ProductSerializer,
        responses={201: ProductSerializer}
    )
    def perform_create(self, serializer):
        serializer.save()
        cache.delete('product_list')  # Invalidate cache on new product

    @swagger_auto_schema(
        operation_description="Update an existing product.",
        request_body=ProductSerializer,
        responses={200: ProductSerializer}
    )
    def perform_update(self, serializer):
        serializer.save()
        cache.delete('product_list')  # Invalidate cache on product update

    @swagger_auto_schema(
        operation_description="Delete a product.",
        responses={204: "No Content"}
    )
    def perform_destroy(self, instance):
        instance.delete()
        cache.delete('product_list')  # Invalidate cache on product deletion
    @swagger_auto_schema(
        operation_description="Create a new product.",
        request_body=ProductSerializer,
        responses={201: ProductSerializer}
    )
    
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Retrieve a list of products.",
        responses={200: ProductSerializer(many=True)}
    )
    
    def list(self, request, *args, **kwargs):
        cached_products = cache.get('product_list')
        if cached_products:
            return Response(cached_products)
        
        response = super().list(request, *args, **kwargs)
        cache.set('product_list', response.data, timeout=300)  # Cache for 5 minutes
        return response
    
    
    # Similarly, decorate other actions as needed