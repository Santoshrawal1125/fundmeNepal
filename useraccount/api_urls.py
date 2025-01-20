from django.urls import path
from .api_views import RegisterAPI,LoginAPI,LogoutAPI

app_name = 'useraccount'
urlpatterns = [
    path('register/', RegisterAPI.as_view(), name='api-register'),
    path('login/', LoginAPI.as_view(), name='api-login'),
    path('logout/', LogoutAPI.as_view(), name='api-logout'),

]
