from django.views import View
from django.shortcuts import render, redirect
from django.contrib import messages
import re
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model, authenticate, login
from django.contrib import auth


class Register(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'akcel/index.html')

    def post(self, request, *args, **kwargs):
        firstname = request.POST.get('firstname', '').strip()
        lastname = request.POST.get('lastname', '').strip()
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '').strip()
        confirmPassword = request.POST.get('confirmPassword', '').strip()

        errors = {}

        if not firstname:
            errors['firstname'] = "First name is required"
        if not lastname:
            errors['lastname'] = "Last name is required"
        if not email:
            errors['email'] = "Email is required"
        elif not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            errors['email'] = "Enter a valid email address"
        elif User.objects.filter(email=email).exists():
            errors['email'] = "Email already exists"

        if not password:
            errors['password'] = "Password is required"
        elif len(password) < 8:
            errors['password'] = "Password must be at least 8 characters"

        if not confirmPassword:
            errors['confirmPassword'] = "Confirm password is required"
        elif password != confirmPassword:
            errors['confirmPassword'] = "Passwords do not match"

        if errors:
            return render(request, 'akcel/index.html', {'errors': errors, 'show_signup_modal': True})

        try:
            user = User.objects.create_user(
                username=email,  # Django requires a username
                first_name=firstname,
                last_name=lastname,
                email=email,
                password=password  # `create_user` automatically hashes it
            )
            messages.success(request, 'Registered successfully')
            return render(request, 'akcel/index.html', {'show_login_modal': True})

        except Exception as e:
            messages.error(request, f'Error: {str(e)}')  # Debugging message
            return render(request, 'akcel/index.html', {'show_signup_modal': True})



class Login(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'akcel/index.html')

    def post(self, request, *args, **kwargs):
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Validate email and password
        if not email or not password:
            messages.error(request, "Both email and password are required")
            return redirect('account:login')

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            messages.error(request, 'Invalid email or password')
            return redirect('account:login')  # Ensure this returns early if the email is not found

            user = authenticate(username=email, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful')
            return render(request, 'akcel/index.html')
        else:
            messages.error(request, 'Invalid email or password')
            return redirect('account:login')


class Logout(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'akcel/index.html')

    def post(self, request, *args, **kwargs):
        auth.logout(request)
        messages.info(request, "Logout successfully")
        return redirect('account:login')
