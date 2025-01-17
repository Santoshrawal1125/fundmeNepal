from django.urls import path
from .api_views import RegisterAPI,LoginAPI,LogoutApi

app_name = 'useraccount'
urlpatterns = [
    path('register/', RegisterAPI.as_view(), name='api-register'),
    path('login/', LoginAPI.as_view(), name='api-login'),
    path('logout/', LogoutApi.as_view(), name='api-logout'),

]
