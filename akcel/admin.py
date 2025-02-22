from django.contrib import admin
from .models import Category, Campaign,ContactUs

# Register your models here.

admin.site.register(Category)
admin.site.register(Campaign)
admin.site.register(ContactUs)