from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from users.views import UserViewSet
from products.views import ProductViewSet, CategoryViewSet
from orders.views import OrderViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

from django.conf import settings
from django.conf.urls.static import static

import debug_toolbar

# Router setup for viewsets
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'products', ProductViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'orders', OrderViewSet)

# Swagger schema view setup
schema_view = get_schema_view(
    openapi.Info(
        title="ecommApp API",
        default_version='v1',
        description="API documentation for the high-load e-commerce backend.",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="b_tursun@kbtu.kz"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    authentication_classes=[],
)

# URL patterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include((router.urls, 'api'), namespace='api')),  # Use the router for all API endpoints
    path('api/auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('__debug__/', include('debug_toolbar.urls')),  # Debug Toolbar
]

# Serve media files in development mode
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
