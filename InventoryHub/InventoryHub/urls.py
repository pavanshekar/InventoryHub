"""
URL configuration for InventoryHub project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from Inventory import views as inventory_views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions as drf_permissions

schema_view = get_schema_view(
   openapi.Info(
      title="InventoryHub API",
      default_version='v1',
      description="API documentation for InventoryHub",
   ),
   public=True,
   permission_classes=(drf_permissions.AllowAny,),
)

router = DefaultRouter()
router.register(r'items', inventory_views.ItemViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('auth/', include('dj_rest_auth.urls')),
    path('auth/registration/', include('dj_rest_auth.registration.urls')),
    path('swagger/', schema_view.without_ui(cache_timeout=0), name='schema-swagger-ui'),  
]
