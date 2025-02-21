from django.shortcuts import render
from django.views import View
from .models import Category, Campaign
from django.http import JsonResponse


class IndexView(View):
    def get(self, request, *args, **kwargs):
        campaigns = Campaign.objects.all()
        categories = Category.objects.all()
        return render(request, 'akcel/index.html', {'campaigns': campaigns, 'categories': categories})


class AboutUsView(View):
    def get(self, request, *args, **kwargs):
        campaigns = Campaign.objects.all()

        return render(request, 'akcel/about-us.html', {'campaigns': campaigns})


class VolunteerView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'akcel/volunteer.html')


class BecomeAVolunteerView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'akcel/become-a-volunteer.html')


class FaqView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'akcel/faq.html')


class AskAQuestionView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'akcel/ask-a-question.html')


class HappyClientsView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'akcel/happy-clients.html')


class HowItWorksView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'akcel/how-it-works.html')


class MissionView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'akcel/mission.html')


class TermsAndConditionView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'akcel/terms-and-condition.html')


class BrowseFundraiserView(View):
    def get(self, request, *args, **kwargs):
        campaigns = Campaign.objects.all()

        return render(request, 'akcel/browse-fundraiser.html', {'campaigns': campaigns})


class BrowseFundraiserCategoryView(View):
    def get(self, request, category, *args, **kwargs):
        # Filter campaigns based on the category name from the Category model
        campaigns = Campaign.objects.filter(category__name__iexact=category)
        return render(request, 'akcel/browse-fundraiser-category.html', {'campaigns': campaigns})


class BecomeAFundraiserView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'akcel/become-a-fundraiser.html')

    def post(self, request, *args, **kwargs):
        # Extract data from the request
        title = request.POST.get('title')
        address = request.POST.get('address')
        city = request.POST.get('city')
        phone_number = request.POST.get('phone_number')
        bank_account_number = request.POST.get('bank_account_number')
        qr_code = request.FILES.get('qr_code')
        image = request.FILES.get('image')
        description = request.POST.get('description')
        goal_amount = request.POST.get('goal_amount')
        citizenship_photo = request.FILES.get('citizenship_photo')
        additional_info = request.POST.get('additional_info')
        created_by = request.user

        # Save to database
        campaign = Campaign.objects.create(
            title=title,
            address=address,
            city=city,
            phone_number=phone_number,
            bank_account_number=bank_account_number,
            qr_code=qr_code,
            image=image,
            description=description,
            goal_amount=goal_amount,
            citizenship_photo=citizenship_photo,
            additional_info=additional_info,
            created_by=created_by
        )
        campaign.save()

        # Respond with a success message
        return JsonResponse({"message": "Form submitted successfully!"})


class FundraiserDetailView(View):
    def get(self, request, slug, *args, **kwargs):
        # Fetch the campaign using the slug
        campaign = Campaign.objects.get(slug=slug)

        # Render the template and pass the campaign to the context
        return render(request, 'akcel/fundraiser-detail.html', {'campaign': campaign})


class ProjectView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'akcel/project.html')


class ProjectCategoriesView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'akcel/project-categories.html')


class ProjectSidebarView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'akcel/project-sidebar.html')


class ProjectStoryView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'akcel/project-story.html')


class ContactUsView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'akcel/contact-us.html')


class Error404View(View):
    def get(self, request, *args, **kwargs):
        return render(request, '404.html')


class BlogView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'akcel/blog.html')


class BlogGridView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'akcel/blog-grid.html')


class BlogListView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'akcel/blog-list.html')


class BlogDetailsView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'akcel/blog-details.html')
