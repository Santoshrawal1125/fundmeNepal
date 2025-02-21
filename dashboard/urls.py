from django.urls import path
from . import views
from .views import *
app_name = 'dashboard'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('update_profile/', views.update_profile, name='update_profile'),
    path('change_password/', views.change_password, name='change_password'),
    path('logout/', views.userlogout, name='logout'),

    # Category
    path('category/', CategoryListView.as_view(), name='product_category'),
    path('category/create/', views.category_create, name='create_category'),
    path('category/update/<int:id>/', views.category_update, name='product_category_update'),
    path('category/delete/', views.categorydelete, name='delete_category'),

    # Rent
    path('rent/', views.rent_list, name='Rent'),
    path('rent/create_or_edit/', views.create_or_edit_rent, name='create_or_edit_rent'),
    path('rent/delete/', views.rent_delete, name='rent_delete'),

    # Contact
    path('contact/', views.contact_list, name='contact_list'),
    path('contact/delete/', views.contact_delete, name='contact_delete'),

    # Inquiry
    path('inquiry/', views.inquiry_list, name='inquiry_list'),
    path('inquiry/delete/', views.inquiry_delete, name='inquiry_delete'),

    # Organization
    path('organization/settings/', views.organization_settings, name='company_detail'),
    path('organization/about/', views.abouts, name='about'),

    # Blog
    path('blog/', views.blog_list, name='blog'),
    path('blog/create/', views.blog_create, name='create_blog'),
    path('blog/update/<int:id>/', views.blog_update, name='blog_update'),
    path('blog/delete/', views.blog_delete, name='blog_delete'),

    # Agent
    path('agent/', views.agent_list, name='agent'),
    path('agent/create/', views.agent_create, name='create_agent'),
    path('agent/update/<int:id>/', views.agent_update, name='agent_update'),
    path('agent/delete/', views.agent_delete, name='agent_delete'),

    # Users
    path('customer', UsersListView.as_view(), name="customer_list"),
    path('customer/delete', views.Userdelete, name='delete_customer'),

    path('fundraiser/<slug:slug>/', AdminFundraiserDetailView.as_view(), name='admin_fundraiser_detail'),
]



