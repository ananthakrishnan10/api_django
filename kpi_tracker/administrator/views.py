from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics, status
from authentication.models import User
from rest_framework.permissions import IsAuthenticated
from .serializer import UserSerializer
from authentication import IsAdminAccessible
import random


def generate_random_unique_id():
    num = random.randint(1000, 10000)
    unique_id = "SY" + str(num)
    try:
        User.objects.get(unique_id=unique_id)
        return generate_random_unique_id()
    except User.DoesNotExist:
        return unique_id


class UserCreateList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, IsAdminAccessible]
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        input_data = request.data
        unique_id = generate_random_unique_id()
        input_data["username"] = unique_id
        input_data["unique_id"] = unique_id
        input_data["role"] = 2
        serializer = UserSerializer(data=input_data)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        res_data = {
            "message": "User has added"
        }
        return Response(res_data, status.HTTP_201_CREATED)


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, IsAdminAccessible]
    queryset = User.objects.all()
    serializer_class = UserSerializer
