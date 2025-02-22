"""
URL configuration for core project.

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
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from django.conf.urls.static import static
from drf_yasg import openapi
from django.conf import settings
from django.conf.urls import handler404

schema_view = get_schema_view(
    openapi.Info(
        title="Your API Documentation",
        default_version='v1',
        description="API documentation for your project",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)



# Override the default 404 handler
handler404 = 'akcel.views.custom_404'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('akcel.urls', namespace='akcel')),
    path('account/', include('useraccount.urls', namespace='account')),
    path('api/user/', include('useraccount.api_urls')),
    path('api/', include('akcel.api_urls')),  # Replace 'your_app_name' with your actual app name
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('dashboard/', include('dashboard.urls')),
    path('khalti/', include('khalti.urls')),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
