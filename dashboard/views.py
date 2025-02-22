from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404
from django.views import View
from akcel.models import Campaign, Category, ContactUs  # Import Campaign and Category models
from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models import Sum
from django.contrib.auth import get_user_model

class AdminFundraiserDetailView(View):
    def get(self, request, slug, *args, **kwargs):
        campaign = get_object_or_404(Campaign, slug=slug)
        return render(request, 'dashboard/category.html', {'campaign': campaign})


def admin_required(user):
    return user.is_staff


@login_required
@user_passes_test(admin_required)
def index(request):
    view = {}
    User = get_user_model()
    # Get the total count of users
    view['user_count'] = User.objects.count()
    

    # Get all campaigns (can be filtered if needed)
    view['campaigns'] = Campaign.objects.all()

    # Get the total sum of 'current_amount' from Campaigns
    view['total_collected'] = Campaign.objects.aggregate(Sum('current_amount'))['current_amount__sum'] or 0

    # Get the count of active campaigns
    view['active_campaigns'] = Campaign.objects.filter(is_active=True).count()

    # Get the count of inactive campaigns
    view['not_active'] = Campaign.objects.filter(is_active=False).count()
    
    view['contact_to_review'] = ContactUs.objects.count()

    view['total_to_collect'] = Campaign.objects.aggregate(Sum('goal_amount'))['goal_amount__sum'] or 0
    return render(request, 'dashboard/base_index/index.html',view)


'''Login Section'''


def login(request):
    return render(request, "dashboard/login/login.html")


'''Update Profile'''


def update_profile(request):
    return render(request, 'dashboard/updateProfile/updateProfile.html')


'''Change password'''


def change_password(request):
    return render(request, 'dashboard/updateProfile/change_password.html')


'''Logout Section'''


def userlogout(request):
    return render(request, 'dashboard/login/login.html')


'''Category Section'''


class CategoryListView(generic.ListView):
    model = Category
    template_name = 'dashboard/category/category.html'
    context_object_name = 'categories'


def category_create(request):
    return render(request, 'dashboard/category/create_category.html')


def category_update(request):
    return render(request, 'dashboard/category/create_category.html')


def categorydelete(request):
    if request.method == "POST":
        id = request.POST.get('category_id')
        instance = get_object_or_404(Category, id=id)
        instance.delete()
        messages.success(request, "Deleted Successfully!")
        return redirect('dashboard:product_category')
    else:
        return redirect('dashboard:product_category')


'''Rent Section'''


class CampaignListView(generic.ListView):
    model = Campaign
    template_name = 'dashboard/rent/rent.html'
    context_object_name = 'categories'


def create_or_edit_rent(request,slug):
    campaign = Campaign.objects.get(slug = slug )
    if request.method == "POST":
        title = request.POST.get("title")
        goal_amount = request.POST.get("goal_amount")
        is_active = request.POST.get("is_active")=="on"
        description = request.POST.get("description")
        campaign.title = title
        campaign.goal_amount = goal_amount
        campaign.description = description
        campaign.is_active = is_active
        campaign.save()
        return redirect("/dashboard/rent/")

    return render(request, 'dashboard/rent/create_rent.html',{"rent_form":campaign})


def rentdelete(request):
    if request.method == "POST":
        id = request.POST.get('campaign_id')
        print(f"Received campaign_id: {id}")  # Debugging statement

        if not id:
            messages.error(request, "No campaign ID provided.")
            return redirect('dashboard:Rent')

        instance = get_object_or_404(Campaign, id=id)
        instance.delete()
        messages.success(request, "Deleted Successfully!")
        return redirect('dashboard:Rent')
    else:
        return redirect('dashboard:Rent')


'''Contact Section'''


class ContactListView(generic.ListView):
    model = ContactUs
    template_name = 'dashboard/contact/contact.html'
    context_object_name = 'contacts'
    paginate_by = 10


# This view is used to delete individual contact
def Contactdelete(request):
    if request.method == "POST":
        id = request.POST.get(
            'contact_id')  # This line retrieves the value of the 'contact_id' field from the POST data. This is typically a hidden input field in an HTML form that contains the ID of the contact to be deleted.
        instance = get_object_or_404(ContactUs,
                                     id=id)  # This line retrieves the contact object from the database using the get_object_or_404 function. It takes two arguments: the model class (Contact) and the ID of the contact. If the contact does not exist, it returns a 404 Not Found error.
        instance.delete()  # This line deletes the retrieved contact object from the database.
        messages.success(request,
                         "Deleted Successfully!")  # This line adds a success message to the current user's session using Django's messaging framework, indicating that the contact was deleted successfully
        return redirect('dashboard:contact_list')
    else:
        return redirect('dashboard:contact_list')


'''Inquiry Section'''


def inquiry_list(request):
    return render(request, 'dashboard/contact/inquiry.html')


def inquiry_delete(request):
    return redirect('dashboard:inquiry_list')


'''Organization detail section'''


def organization_settings(request):
    return render(request, 'dashboard/organization/organizationDetail_create.html')


def abouts(request):
    return render(request, 'dashboard/organization/create_about.html')


'''Blog Section'''


def blog_list(request):
    return render(request, 'dashboard/blog/blog.html')


def blog_create(request):
    return render(request, 'dashboard/blog/create_blog.html')


def blog_update(request):
    return render(request, 'dashboard/blog/create_blog.html')


def blog_delete(request):
    return redirect('dashboard:blog')


'''Agent Section'''


def agent_list(request):
    return render(request, 'dashboard/agent/agent.html')


def agent_create(request):
    return render(request, 'dashboard/agent/create_agent.html')


def agent_update(request):
    return render(request, 'dashboard/agent/create_agent.html')


def agent_delete(request):
    return redirect('dashboard:agent')


'''Users Section'''


class UsersListView(generic.ListView):
    model = User
    template_name = 'dashboard/user/customer.html'
    context_object_name = 'users'


def Userdelete(request):
    if request.method == "POST":
        id = request.POST.get(
            'user_id')
        instance = get_object_or_404(User, id=id)
        instance.delete()
        messages.success(request, "Deleted Successfully!")
        return redirect('dashboard:customer_list')
    else:
        return redirect('dashboard:customer_list')
