from django.contrib import admin
from .models import Category, Campaign,ContactUs,Donation

# Register your models here.

admin.site.register(Category)
admin.site.register(Campaign)
admin.site.register(ContactUs)
admin.site.register(Donation)