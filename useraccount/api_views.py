from rest_framework.views import APIView
from .serializers import UserSerializers
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login, logout
from rest_framework.permissions import AllowAny
from django.views.decorators.csrf import csrf_exempt


class RegisterAPI(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "user registered successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginAPI(APIView):

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        if not email or not password:
            return Response({"error": "Email and password are required"})

        user = authenticate(username=email, password=password)
        if user is not None:
            login(request, user)
            return Response({"message": "Login successful"}, status=status.HTTP_200_OK)
        return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)


class LogoutApi(APIView):

    def post(self, request):
        logout(request)
        return Response({"message": "logout successful"}, status=status.HTTP_200_OK)
