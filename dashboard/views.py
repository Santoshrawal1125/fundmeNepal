from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404
from django.views import View
from akcel.models import Campaign, Category  # Import Campaign and Category models
from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test





class AdminFundraiserDetailView(View):
    def get(self, request, slug, *args, **kwargs):
        campaign = get_object_or_404(Campaign, slug=slug)
        return render(request, 'dashboard/category.html', {'campaign': campaign})




def admin_required(user):
    return user.is_staff

@login_required
@user_passes_test(admin_required)
def index(request):
    return render(request, 'dashboard/base_index/index.html')


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


def rent_list(request):
    campaigns = Campaign.objects.all()
    return render(request, 'dashboard/rent/rent.html', {'campaigns': campaigns})


def create_or_edit_rent(request, rent_id=None):
    return render(request, 'dashboard/rent/create_rent.html')


def rent_delete(request):
    return redirect('dashboard:Rent')


'''Contact Section'''


def contact_list(request):
    return render(request, 'dashboard/contact/contact.html')


def contact_delete(request):
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
