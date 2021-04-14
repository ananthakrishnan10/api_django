from django.shortcuts import render

from pyexcel_xlsx import get_data
from rest_framework.generics import CreateAPIView
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.views import APIView

from authentication.models import User
from rest_framework.permissions import IsAuthenticated, AllowAny

from .models import FileData
from .serializer import UserSerializer, FileSerializer, DataSerializer
from authentication import IsAdminAccessible
import random
import json


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
        res_data = {"message": "User added successfully"}
        return Response(res_data, status.HTTP_201_CREATED)


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, IsAdminAccessible]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class FileView(CreateAPIView):
    permission_classes = [IsAuthenticated, IsAdminAccessible]
    serializer_class = FileSerializer
    parser_classes = [MultiPartParser]

    def create(self, request, format=None):
        serializer = FileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            data = get_data(request.data["file"])
            data = (json.loads(json.dumps(data)))["Sheet1"]
            serializers_data = []
            for d in data[1:]:
                try:
                    input_data = {
                        "file_id": serializer.data["id"],
                        "month": d[0],
                        "month_actual": d[1],
                        "month_target": d[2],
                        "ytd_actual": d[3],
                        "ytd_target": d[4],
                    }
                    dataSerializer = DataSerializer(data=input_data)
                    dataSerializer.is_valid(raise_exception=True)
                    self.perform_create(dataSerializer)
                    serializers_data.append(dataSerializer.data)
                except:
                    res_data = {"message": "Data is not complete"}
                    return Response(res_data, status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        res_data = {"message": "File upload successfully", "data": serializers_data}
        return Response(res_data, status.HTTP_200_OK)


class DataList(generics.ListAPIView):
    queryset = FileData.objects.order_by("-id")[:1]
    serializer_class = DataSerializer
    permission_classes = [IsAuthenticated, IsAdminAccessible]

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = DataSerializer(queryset, many=True)
        file_id = json.loads(json.dumps(serializer.data[0]))["file_id"]
        data = FileData.objects.filter(file_id=file_id)
        serializer = DataSerializer(data, many=True)
        return Response(serializer.data, status.HTTP_200_OK)
