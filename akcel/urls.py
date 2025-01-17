from django.urls import path, include
from . import views
from .views import *

app_name = 'akcel'

urlpatterns = [

    path('', views.index, name="index"),
    path('index/', views.index, name="index"),

    path('about-us/', views.about_us, name="about-us"),
    path('volunteer/', views.volunteer, name="volunteer"),
    path('become-a-volunteer/', views.become_a_volunteer, name="become-a-volunteer"),
    path('faq/', views.faq, name="faq"),
    path('ask-a-question/', views.ask_a_question, name="ask-a-question"),
    path('happy-clients/', views.happy_clients, name="happy-clients"),
    path('how-it-works/', views.how_it_works, name="how-it-works"),
    path('mission/', views.mission, name="mission"),
    path('terms-and-condition/', views.terms_and_condition, name="terms-and-condition"),

    path('browse-fundraiser/', views.browse_fundraiser, name="browse-fundraiser"),
    path('become-a-fundraiser/', views.become_a_fundraiser, name="become-a-fundraiser"),
    path('fundraiser-detail/', views.fundraiser_detail, name="fundraiser-detail"),

    path('project/', views.project, name="project"),
    path('project-categories/', views.project_categories, name="project-categories"),
    path('project-sidebar/', views.project_sidebar, name="project-sidebar"),
    path('project-story/', views.project_story, name="project-story"),


    path('contact-us/', views.contact_us, name="contact-us"),
    path('error-404/', views.error_404, name="error-404"),

    path('blog/', views.blog, name="blog"),
    path('blog-grid/', views.blog_grid, name="blog-grid"),
    path('blog-list/', views.blog_list, name="blog-list"),
    path('blog-details/', views.blog_details, name="blog-details"),

]
