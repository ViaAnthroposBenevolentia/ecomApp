from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    
    # email = models.EmailField(unique=True)
    # phone_number = models.CharField(max_length=15, blank=True, null=True)
    # address = models.TextField(blank=True, null=True)
    # date_of_birth = models.DateField(blank=True, null=True)
    # is_verified = models.BooleanField(default=False)
    
    # Additional fields for e-commerce
    # shipping_address = models.TextField(blank=True, null=True)
    # billing_address = models.TextField(blank=True, null=True)
    # preferred_payment_method = models.CharField(max_length=50, blank=True, null=True)
    
    # Customer loyalty
    # loyalty_points = models.IntegerField(default=0)
    
    # Newsletter subscription
    # subscribe_newsletter = models.BooleanField(default=False)
    
    def __str__(self):
        return self.username