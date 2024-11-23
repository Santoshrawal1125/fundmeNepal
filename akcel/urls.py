from akcel import akcel_views
from django.urls import path, include


app_name = 'akcel'
urlpatterns = [

    path('', akcel_views.index, name="index"),
    path('index/', akcel_views.index, name="index"),
    path('index-2/', akcel_views.index_2, name="index-2"),
    path('index-3/', akcel_views.index_3, name="index-3"),

    path('about-us/', akcel_views.about_us, name="about-us"),
    path('volunteer/', akcel_views.volunteer, name="volunteer"),
    path('become-a-volunteer/', akcel_views.become_a_volunteer, name="become-a-volunteer"),
    path('faq/', akcel_views.faq, name="faq"),
    path('certificates/', akcel_views.certificates, name="certificates"),
    path('ask-a-question/', akcel_views.ask_a_question, name="ask-a-question"),
    path('happy-clients/', akcel_views.happy_clients, name="happy-clients"),
    path('how-it-works/', akcel_views.how_it_works, name="how-it-works"),
    path('mission/', akcel_views.mission, name="mission"),
    path('terms-and-condition/', akcel_views.terms_and_condition, name="terms-and-condition"),

    path('browse-fundraiser/', akcel_views.browse_fundraiser, name="browse-fundraiser"),
    path('become-a-fundraiser/', akcel_views.become_a_fundraiser, name="become-a-fundraiser"),
    path('fundraiser-detail/', akcel_views.fundraiser_detail, name="fundraiser-detail"),

    path('project/', akcel_views.project, name="project"),
    path('project-categories/', akcel_views.project_categories, name="project-categories"),
    path('project-sidebar/', akcel_views.project_sidebar, name="project-sidebar"),
    path('project-story/', akcel_views.project_story, name="project-story"),

    path('blog/', akcel_views.blog, name="blog"),
    path('blog-grid/', akcel_views.blog_grid, name="blog-grid"),
    path('blog-list/', akcel_views.blog_list, name="blog-list"),
    path('blog-details/', akcel_views.blog_details, name="blog-details"),

    path('contact-us/', akcel_views.contact_us, name="contact-us"),
    path('coming-soon/', akcel_views.coming_soon, name="coming-soon"),
    path('under-maintenance/', akcel_views.under_maintenance, name="under-maintenance"),
    path('error-404/', akcel_views.error_404, name="error-404"),

]
