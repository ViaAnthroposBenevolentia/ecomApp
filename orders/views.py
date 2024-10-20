from rest_framework import viewsets, permissions
from .models import Order
from .serializers import OrderSerializer
from django.db import transaction
from .tasks import send_order_confirmation_email

class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Order.objects.all()

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            # queryset just for schema generation metadata
            return Order.objects.none()
        
        user = self.request.user
        if user.is_staff:
            return Order.objects.all()
        
        return Order.objects.filter(user=self.request.user).prefetch_related('items__product')

    @transaction.atomic
    def perform_create(self, serializer):
        with transaction.atomic():
            order = serializer.save(user=self.request.user)
            send_order_confirmation_email.delay(order.id)