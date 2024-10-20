from celery import shared_task
from django.core.mail import send_mail
from .models import Order
from django.conf import settings

@shared_task(bind=True, max_retries=3)
def send_order_confirmation_email(order_id, _):
    try:
        order = Order.objects.get(id=order_id)
        subject = f"Order Confirmation - Order #{order.id}"
        message = f"Dear {order.user.first_name},\n\nYour order has been placed successfully.\n\nOrder Details:\n"
        for item in order.items.all():
            message += f"- {item.product.name} (Quantity: {item.quantity})\n"
        message += "\nThank you for shopping with us!"
        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [order.user.email],
            fail_silently=False,
        )
    except Order.DoesNotExist:
        # Handle case where order does not exist
        pass
    except Exception as e:
        # Log exception
        pass
