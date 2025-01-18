from django.views import View
from django.shortcuts import render, redirect
from django.contrib import messages
import re
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model, authenticate, login
from .serializers import UserSerializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib import auth


class Register(APIView):

    def get(self, request, *args, **kwargs):
        return render(request, 'akcel/index.html')

    def post(self, request, *args, **kwargs):
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmPassword = request.POST.get('confirmPassword')

        # basic validations to check if it is valid or not

        if not firstname or not lastname or not email or not password or not confirmPassword:
            messages.error(request, 'All fields are required')
            return redirect('account:register')

        if len(password) < 8:
            messages.error(request, 'Password must be least 8 letters')
            return redirect('account:register')

        if password != confirmPassword:
            messages.error(request, 'password and confirm password do not match')
            return redirect('account:register')

        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            messages.error(request, 'Enter a valid email address!')
            return redirect('account:register')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'email already exists')
            return redirect('account:register')

        try:
            user = User.objects.create_user(
                username=email,  # changed django user default username to email as we login with emai not username
                first_name=firstname,
                last_name=lastname,
                password=password,
                email=email
            )
            user.save()
            messages.success(request, 'Registered successfully')
            # Redirect with a query parameter to trigger the login modal
            return render(request, 'akcel/index.html', {'show_login_modal': True})

        except Exception as e:
            messages.error(request, 'An error occurred during registration')
            return redirect('account:register')


class Login(APIView):

    def get(self, request, *args, **kwargs):
        return render(request, 'akcel/index.html')

    def post(self, request, *args, **kwargs):

        email = request.POST.get('email')
        password = request.POST.get('password')

        # validate email and password
        if not email or not password:
            messages.error(request, "Both email and pass are required")
            return redirect('account:login')

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            messages.error(request, 'email and password invalid')

        user = authenticate(username=email, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Login success')
            return render(request, 'akcel/index.html')

        else:
            messages.error(request, 'Login Not success')
            return render(request, 'akcel/index.html')


class Logout(APIView):

    def get(self, request, *args, **kwargs):
        return render(request, 'akcel/index.html')

    def post(self, request, *args, **kwargs):
        auth.logout(request)
        messages.info(request,"Logout successfully")
        return redirect('account:login')
