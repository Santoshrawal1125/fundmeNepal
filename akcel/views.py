from django.shortcuts import render


def index(request):
    context = {
        "page_title": "Home 1"
    }
    return render(request, 'akcel/index.html', context)


def about_us(request):
    context = {
        "page_title": "About Us"
    }
    return render(request, 'akcel/about-us.html', context)


def volunteer(request):
    context = {
        "page_title": "Volunteer"
    }
    return render(request, 'akcel/volunteer.html', context)


def become_a_volunteer(request):
    context = {
        "page_title": "Become A Volunteer"
    }
    return render(request, 'akcel/become-a-volunteer.html', context)


def faq(request):
    context = {
        "page_title": "FAQ"
    }
    return render(request, 'akcel/faq.html', context)


def ask_a_question(request):
    context = {
        "page_title": "Ask A Question"
    }
    return render(request, 'akcel/ask-a-question.html', context)


def happy_clients(request):
    context = {
        "page_title": "Happy Clients"
    }
    return render(request, 'akcel/happy-clients.html', context)


def how_it_works(request):
    context = {
        "page_title": "How It Works"
    }
    return render(request, 'akcel/how-it-works.html', context)


def mission(request):
    context = {
        "page_title": "Mission"
    }
    return render(request, 'akcel/mission.html', context)


def terms_and_condition(request):
    context = {
        "page_title": "Terms And Condition"
    }
    return render(request, 'akcel/terms-and-condition.html', context)


def browse_fundraiser(request):
    context = {
        "page_title": "Browse Fundraiser"
    }
    return render(request, 'akcel/browse-fundraiser.html', context)


def become_a_fundraiser(request):
    context = {
        "page_title": "Become A Fundraiser"
    }
    return render(request, 'akcel/become-a-fundraiser.html', context)


def fundraiser_detail(request):
    context = {
        "page_title": "Fundraiser Detail"
    }
    return render(request, 'akcel/fundraiser-detail.html', context)


def project(request):
    context = {
        "page_title": "Project"
    }
    return render(request, 'akcel/project.html', context)


def project_categories(request):
    context = {
        "page_title": "Project Categories"
    }
    return render(request, 'akcel/project-categories.html', context)


def project_sidebar(request):
    context = {
        "page_title": "Project Sidebar"
    }
    return render(request, 'akcel/project-sidebar.html', context)


def project_story(request):
    context = {
        "page_title": "Project Story"
    }
    return render(request, 'akcel/project-story.html', context)


def contact_us(request):
    context = {
        "page_title": "Contact Us"
    }
    return render(request, 'akcel/contact-us.html', context)


def error_404(request):
    context = {
        "page_title": "Error 404"
    }
    return render(request, '404.html', context)


def blog(request):
    context = {
        "page_title": "Blog"
    }
    return render(request, 'akcel/blog.html', context)


def blog_grid(request):
    context = {
        "page_title": "Blog Grid"
    }
    return render(request, 'akcel/blog-grid.html', context)


def blog_list(request):
    context = {
        "page_title": "Blog List"
    }
    return render(request, 'akcel/blog-list.html', context)


def blog_details(request):
    context = {
        "page_title": "Blog Details"
    }
    return render(request, 'akcel/blog-details.html', context)
