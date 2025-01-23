# from .models import Category, Campaign
#
#
# def global_context(request):
#     categories = Category.objects.all()
#     campaigns = Campaign.objects.all()
#     return {
#         "page_title": "Global Page Title",  # Set a global page title here
#         "categories": categories,
#         "campaigns": campaigns,
#     }
#
#
# # If you want specific page titles in each view, you can create a function for each view title
# def index_context(request):
#     return {
#         "page_title": "Home 1"
#     }
#
#
# def about_us_context(request):
#     return {
#         "page_title": "About Us"
#     }
#
#
# def volunteer_context(request):
#     return {
#         "page_title": "Volunteer"
#     }
#
#
# def become_a_volunteer_context(request):
#     return {
#         "page_title": "Become A Volunteer"
#     }
#
#
# def faq_context(request):
#     return {
#         "page_title": "FAQ"
#     }
#
#
# def ask_a_question_context(request):
#     return {
#         "page_title": "Ask A Question"
#     }
#
#
# def happy_clients_context(request):
#     return {
#         "page_title": "Happy Clients"
#     }
#
#
# def how_it_works_context(request):
#     return {
#         "page_title": "How It Works"
#     }
#
#
# def mission_context(request):
#     return {
#         "page_title": "Mission"
#     }
#
#
# def terms_and_condition_context(request):
#     return {
#         "page_title": "Terms And Condition"
#     }
#
#
# def browse_fundraiser_context(request):
#     return {
#         "page_title": "Browse Fundraiser"
#     }
#
#
# def become_a_fundraiser_context(request):
#     return {
#         "page_title": "Become A Fundraiser"
#     }
#
#
# def fundraiser_detail_context(request):
#     return {
#         "page_title": "Fundraiser Detail"
#     }
#
#
# def project_context(request):
#     return {
#         "page_title": "Project"
#     }
#
#
# def project_categories_context(request):
#     return {
#         "page_title": "Project Categories"
#     }
#
#
# def project_sidebar_context(request):
#     return {
#         "page_title": "Project Sidebar"
#     }
#
#
# def project_story_context(request):
#     return {
#         "page_title": "Project Story"
#     }
#
#
# def contact_us_context(request):
#     return {
#         "page_title": "Contact Us"
#     }
#
#
# def error_404_context(request):
#     return {
#         "page_title": "Error 404"
#     }
#
#
# def blog_context(request):
#     return {
#         "page_title": "Blog"
#     }
#
#
# def blog_grid_context(request):
#     return {
#         "page_title": "Blog Grid"
#     }
#
#
# def blog_list_context(request):
#     return {
#         "page_title": "Blog List"
#     }
#
#
# def blog_details_context(request):
#     return {
#         "page_title": "Blog Details"
#     }
