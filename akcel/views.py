from django.shortcuts import render,redirect
from django.views import View
from .models import Category, Campaign, ContactUs
from django.http import JsonResponse
from useraccount.decorators import login_required
import requests,random
from django.conf import settings

class IndexView(View):
    def get(self, request, *args, **kwargs):
        campaigns = Campaign.objects.filter(days_left__gte=0,is_active=True)
        categories = Category.objects.all()
        return render(request, 'akcel/index.html', {'campaigns': campaigns, 'categories': categories})

def custom_404(request,exception):
    return render(request,'404.html',status=404)

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
        query = request.GET.get("query","").strip()
        if query:
            campaigns = search_items(request)
        else:
            campaigns = Campaign.objects.filter(days_left__gte=0,is_active=True)
        return render(request, 'akcel/browse-fundraiser.html', {'campaigns': campaigns})

def search_items(request):
    if request.method == "GET":
        query = request.GET["query"]
        if query != "":
            search_campaigns = Campaign.objects.filter(title__icontains = query,days_left__gte=0,is_active=True)
            return search_campaigns
        else:
            return []
        
class BrowseFundraiserCategoryView(View):
    def get(self, request, category, *args, **kwargs):
        # Filter campaigns based on the category name from the Category model
        query = request.GET.get("query","").strip()
        if query:
            campaigns = search_items_category_wise(request,category)
        else:
            campaigns = Campaign.objects.filter(category__name__iexact=category,days_left__gte=0,is_active=True)
        return render(request, 'akcel/browse-fundraiser-category.html', {'campaigns': campaigns})

def search_items_category_wise(request,category):
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
            show_login_modal=True
        else:
            show_login_modal=False
        return render(request, 'akcel/become-a-fundraiser.html',{"show_login_modal_stick":show_login_modal})

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
    def post(self,request,*args,**kwargs): 
        fullname = request.POST.get("fullname")
        email = request.POST.get("email")
        phone_number = request.POST.get("phonenumber")
        message = request.POST.get("message")

        ContactUs.objects.create(
        full_name = fullname,
        email = email,
        contact_number = phone_number,
        message = message
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
    # Generate a unique purchase_order_id (this can be a random ID or related to the transaction)
    purchase_order_id = "Order" + str(random.randint(1000, 9999))
    
    payload = {
        "return_url": "http://127.0.0.1:8000/payment/",  # your return URL after payment
        "website_url": "http://127.0.0.1:8000/",  # your website URL
        "amount": 1300,  # amount in paisa
        "purchase_order_id": purchase_order_id,
        "purchase_order_name": "Test Product",
    }
    
    headers = {
        "Authorization": "Key " + settings.KHALTI_API_KEY,  # Your Khalti API key
        "Content-Type": "application/json"
    }

    # Send POST request to initiate payment
    response = requests.post("https://dev.khalti.com/api/v2/epayment/initiate/", json=payload, headers=headers)

    if response.status_code == 200:
        data = response.json()
        payment_url = data['payment_url']
        return redirect(payment_url)
    else:
        return JsonResponse({"error": "Payment initiation failed"}, status=500)
    

def payment_callback(request):
    pidx = request.GET.get('pidx')
    txn_id = request.GET.get('txnId')
    status = request.GET.get('status')

    # Now, check the payment status by calling the lookup API
    lookup_payload = {"pidx": pidx}
    headers = {
        "Authorization": "Key " + settings.KHALTI_API_KEY,  # Your Khalti API key
        "Content-Type": "application/json"
    }

    response = requests.post("https://dev.khalti.com/api/v2/epayment/lookup/", json=lookup_payload, headers=headers)

    if response.status_code == 200:
        data = response.json()
        if data['status'] == "Completed":
            # Payment successful
            return JsonResponse({"message": "Payment Successful"})
        else:
            # Payment failed or pending
            return JsonResponse({"message": "Payment failed or pending"})
    else:
        return JsonResponse({"error": "Failed to verify payment status"}, status=500)