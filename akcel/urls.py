from django.urls import path
from .views import *
app_name = 'akcel'

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('about-us/', AboutUsView.as_view(), name="about-us"),
    path('volunteer/', VolunteerView.as_view(), name="volunteer"),
    path('become-a-volunteer/', BecomeAVolunteerView.as_view(), name="become-a-volunteer"),
    path('faq/', FaqView.as_view(), name="faq"),
    path('ask-a-question/', AskAQuestionView.as_view(), name="ask-a-question"),
    path('happy-clients/', HappyClientsView.as_view(), name="happy-clients"),
    path('how-it-works/', HowItWorksView.as_view(), name="how-it-works"),
    path('mission/', MissionView.as_view(), name="mission"),
    path('terms-and-condition/', TermsAndConditionView.as_view(), name="terms-and-condition"),
    path('browse-fundraiser/', BrowseFundraiserView.as_view(), name="browse-fundraiser"),
    path('become-a-fundraiser/', BecomeAFundraiserView.as_view(), name="become-a-fundraiser"),
    path('fundraiser-detail/<slug:slug>/', FundraiserDetailView.as_view(), name="fundraiser-detail"),
    path('project/', ProjectView.as_view(), name="project"),
    path('project-categories/', ProjectCategoriesView.as_view(), name="project-categories"),
    path('project-sidebar/', ProjectSidebarView.as_view(), name="project-sidebar"),
    path('project-story/', ProjectStoryView.as_view(), name="project-story"),
    path('contact-us/', ContactUsView.as_view(), name="contact-us"),
    path('error-404/', Error404View.as_view(), name="error-404"),
    path('blog/', BlogView.as_view(), name="blog"),
    path('blog-grid/', BlogGridView.as_view(), name="blog-grid"),
    path('blog-list/', BlogListView.as_view(), name="blog-list"),
    path('blog-details/', BlogDetailsView.as_view(), name="blog-details"),
    path('fundraiser-details-category/<slug:slug>/', FundraiserDetailsCategory.as_view(), name="fundraiser-details-category"),

]
