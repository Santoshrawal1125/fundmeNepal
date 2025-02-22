from django.shortcuts import render, redirect
from django.views import View
from .models import Category, Campaign, ContactUs, Donation
from django.http import JsonResponse
from useraccount.decorators import login_required
import requests, random
from django.conf import settings
from django.shortcuts import get_object_or_404
from django.urls import reverse


class IndexView(View):
    def get(self, request, *args, **kwargs):
        campaigns = Campaign.objects.filter(days_left__gte=0,is_active=True)
        categories = Category.objects.all()
        return render(request, 'akcel/index.html', {'campaigns': campaigns, 'categories': categories})


def custom_404(request, exception):
    return render(request, '404.html', status=404)


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
        query = request.GET.get("query", "").strip()
        if query:
            campaigns = search_items(request)
        else:
            campaigns = Campaign.objects.filter(days_left__gte=0,is_active=True)
        return render(request, 'akcel/browse-fundraiser.html', {'campaigns': campaigns})


def search_items(request):
    if request.method == "GET":
        query = request.GET["query"]
        if query != "":
            search_campaigns = Campaign.objects.filter(title__icontains=query)

            search_campaigns = Campaign.objects.filter(title__icontains = query,days_left__gte=0,is_active=True)

            return search_campaigns
        else:
            return []


class BrowseFundraiserCategoryView(View):
    def get(self, request, category, *args, **kwargs):
        # Filter campaigns based on the category name from the Category model
        query = request.GET.get("query", "").strip()
        if query:
            campaigns = search_items_category_wise(request, category)
        else:
            campaigns = Campaign.objects.filter(category__name__iexact=category,days_left__gte=0,is_active=True)
        return render(request, 'akcel/browse-fundraiser-category.html', {'campaigns': campaigns})


def search_items_category_wise(request, category):
    if request.method == "GET":
        query = request.GET["query"]
        if query != "":


            search_campaigns = Campaign.objects.filter(title__icontains = query , category__name__iexact=category ,is_active=True,days_left__gte=0)

            return search_campaigns
        else:
            return []


class BecomeAFundraiserView(View):
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            show_login_modal = True
        else:
            show_login_modal = False
        return render(request, 'akcel/become-a-fundraiser.html', {"show_login_modal_stick": show_login_modal})

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
            created_by=created_by,
        )
        campaign.save()
        return redirect("/")
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

    def post(self, request, *args, **kwargs):
        fullname = request.POST.get("fullname")
        email = request.POST.get("email")
        phone_number = request.POST.get("phonenumber")
        message = request.POST.get("message")

        ContactUs.objects.create(
            full_name=fullname,
            email=email,
            contact_number=phone_number,
            message=message
        )

        return redirect("/contact-us/")


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


def initiate_payment(request):
    if request.method == "POST":
        amount = int(request.POST.get('amount')) * 100  # Convert to paisa
        campaign_id = request.POST.get('campaign_id')

        khalti_url = "https://khalti.com/api/v2/epayment/initiate/"
        return_url = request.build_absolute_uri(reverse("akcel:payment_callback"))

        payload = {
            "return_url": return_url,  # Callback URL
            "website_url": request.build_absolute_uri("/"),
            "amount": amount,
            "purchase_order_id": f"Order{campaign_id}",
            "purchase_order_name": "Campaign Donation",
        }

        headers = {
            "Authorization": f"Key {settings.KHALTI_API_KEY}",
            "Content-Type": "application/json"
        }

        response = requests.post(khalti_url, json=payload, headers=headers)

        if response.status_code == 200:
            payment_data = response.json()
            return redirect(payment_data["payment_url"])  # Redirect to Khalti
        else:
            return JsonResponse({"error": "Failed to initiate payment"}, status=400)

    return redirect("index")


def payment_callback(request):
    pidx = request.GET.get('pidx')
    txn_id = request.GET.get('transaction_id')
    status = request.GET.get('status')
    amount = request.GET.get('amount')  # In paisa
    campaign_id = request.GET.get('purchase_order_id').replace("Order", "")

    campaign = get_object_or_404(Campaign, id=campaign_id)
    amount_in_rs = int(amount) / 100  # Convert from paisa to rupees

    lookup_payload = {"pidx": pidx}
    headers = {
        "Authorization": "Key " + settings.KHALTI_API_KEY,
        "Content-Type": "application/json"
    }

    response = requests.post("https://khalti.com/api/v2/epayment/lookup/", json=lookup_payload, headers=headers)

    if response.status_code == 200:
        data = response.json()
        if data["status"] == "Completed":
            campaign.current_amount += amount_in_rs
            campaign.save()

            Donation.objects.create(
                user=request.user if request.user.is_authenticated else None,
                campaign=campaign,
                amount=amount_in_rs,
                transaction_id=txn_id
            )

            return redirect("index")  # Redirect to homepage after successful payment
        else:
            return JsonResponse({"message": "Payment failed or pending"})

    return JsonResponse({"error": "Failed to verify payment status"}, status=500)
