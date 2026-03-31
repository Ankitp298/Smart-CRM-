from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import AuthenticationFailed
from .serializers import RegisterSerializer,LoginSerializer

# Create your views here.
# Genrate Token 
def get_tokens_for_user(user):
    if not user.is_active:
      raise AuthenticationFailed("User is not active")
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data = request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"message" : "User Registered Successfully"},status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    
class LoginView(APIView):
    def post(self,request):
        serializer = LoginSerializer(data = request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            token = get_tokens_for_user(user)
            return Response({"token":token,
                             "email": user.email,
                             "role": user.role}
                             ,status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)