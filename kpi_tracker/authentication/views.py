from django.contrib.auth import authenticate
from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.generics import get_object_or_404, GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from kpi_tracker.settings import SECRET_KEY
from .models import User
import jwt
from .serializer import LoginResponseSerializer, SignupSerializer
import random


def generate_random_unique_id():
    num = random.randint(1000, 10000)
    unique_id = "SY" + str(num)
    try:
        User.objects.get(unique_id=unique_id)
        return generate_random_unique_id()
    except User.DoesNotExist:
        return unique_id


class AuthObj(object):
    def __init__(self, access_token, refresh_token):
        self.access_token = access_token
        self.refresh_token = refresh_token


class LoginRespObj(object):
    def __init__(self, access_token, refresh_token, user):
        self.authorization = AuthObj(
            access_token=access_token, refresh_token=refresh_token
        )
        self.user = user


class LoginAPIView(APIView):
    permission_classes = [AllowAny]

    @staticmethod
    def post(request):
        data = request.data

        try:
            email = data["email"]
            password = data["password"]
            _user = get_object_or_404(User, email=email)
        except:
            resp = {
                "message": "email not found",
            }
            return Response(resp, status=status.HTTP_404_NOT_FOUND)

        try:
            user = get_object_or_404(User, email=email, password=password)

        except:
            resp = {
                "message": "Incorrect password",
            }
            return Response(resp, status=status.HTTP_404_NOT_FOUND)
        token = RefreshToken.for_user(user)
        access_token = token.access_token
        access_token["email"] = user.email
        access_token["username"] = user.username
        access_token["id"] = user.id
        access_token["first_name"] = user.first_name
        access_token["last_name"] = user.last_name
        refresh_token = token
        login_response_obj = LoginRespObj(access_token, refresh_token, user)
        login_response = LoginResponseSerializer(login_response_obj).data
        login_response["email"] = user.email
        login_response["username"] = user.username
        login_response["id"] = user.id
        login_response["first_name"] = user.first_name
        login_response["last_name"] = user.last_name
        return Response(login_response, status=status.HTTP_200_OK)


class RegisterView(APIView):
    permission_classes = [AllowAny]

    @staticmethod
    def post(request):
        input_data = request.data
        unique_id = generate_random_unique_id()
        input_data["username"] = unique_id
        input_data["unique_id"] = unique_id
        input_data["role"] = 2
        print(input_data)
        serializer = SignupSerializer(data=input_data)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.get(email=input_data["email"])

        token = RefreshToken.for_user(user)
        access_token = token.access_token
        access_token["email"] = user.email
        access_token["username"] = user.username
        access_token["id"] = user.id
        access_token["first_name"] = user.first_name
        access_token["last_name"] = user.last_name
        refresh_token = token
        login_response_obj = LoginRespObj(access_token, refresh_token, user)
        login_response = LoginResponseSerializer(login_response_obj).data
        login_response["email"] = user.email
        login_response["username"] = user.username
        login_response["id"] = user.id
        login_response["first_name"] = user.first_name
        login_response["last_name"] = user.last_name
        return Response(login_response, status=status.HTTP_200_OK)


class RefreshTokenView(APIView):
    permission_classes = [AllowAny]

    @staticmethod
    def post(request):
        data = request.data["refresh_token"]
        try:
            payload = jwt.decode(data, SECRET_KEY, "HS256")
        except:
            data = {
                "message": "Signature has expired",
            }
            return Response(data, status.HTTP_400_BAD_REQUEST)
        try:
            user = User.objects.get(id=payload["id"])
            print(user)
        except:
            response = {"message": "User not found"}
            return Response(response, status.HTTP_404_NOT_FOUND)
        token = RefreshToken.for_user(user)
        access_token = token.access_token
        access_token["email"] = user.email
        access_token["username"] = user.username
        access_token["id"] = user.id
        access_token["first_name"] = user.first_name
        access_token["last_name"] = user.last_name
        refresh_token = token
        login_response_obj = LoginRespObj(access_token, refresh_token, user)
        login_response = LoginResponseSerializer(login_response_obj).data
        return Response(login_response, status=status.HTTP_200_OK)
