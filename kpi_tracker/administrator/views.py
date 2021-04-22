import os
import pandas
from django.http import Http404
from rest_framework.generics import CreateAPIView
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.views import APIView

from authentication.models import User
from rest_framework.permissions import IsAuthenticated, AllowAny

from .models import FileData
from .serializer import (
    UserSerializer,
    FileSerializer,
    DataSerializer,
    UpdateUserSerializer,
)
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


class UserDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = UserSerializer(snippet)
        return Response(serializer.data, status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = UpdateUserSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            res_data = {"message": "User updated successfully", "data": serializer.data}
            return Response(res_data, status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        res_data = {"message": "User deleted successfully"}
        return Response(res_data, status.HTTP_200_OK)


class FileView(CreateAPIView):
    # permission_classes = [IsAuthenticated, IsAdminAccessible]
    permission_classes = [AllowAny]
    serializer_class = FileSerializer
    parser_classes = [MultiPartParser]

    def create(self, request, format=None):
        serializer = FileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            req_data = request.FILES["file"]
            file_extension = os.path.splitext(req_data.name)[1]

            if file_extension == ".xlsx":
                df = pandas.read_excel(req_data, engine="openpyxl")
            elif file_extension == ".xls":
                df = pandas.read_excel(req_data)
            elif file_extension == ".csv":
                df = pandas.read_csv(req_data.name)
            else:
                raise Exception("File not supported")
            serializers_data = []
            for index, row in df.iterrows():
                try:
                    input_data = {
                        "file_id": serializer.data["id"],
                        "month": row[0],
                        "month_actual": row[1],
                        "month_target": row[2],
                        "ytd_actual": row[3],
                        "ytd_target": row[4],
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
        res_data = {
            "message": "File upload successfully",
            "file_id": serializer.data["id"],
            "data": serializers_data,
        }
        return Response(res_data, status.HTTP_200_OK)


class DataList(generics.ListAPIView):
    queryset = FileData.objects.order_by("-id")[:1]
    serializer_class = DataSerializer
    # permission_classes = [IsAuthenticated, IsAdminAccessible]
    permission_classes = [AllowAny]

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = DataSerializer(queryset, many=True)
        file_id = json.loads(json.dumps(serializer.data[0]))["file_id"]
        data = FileData.objects.filter(file_id=file_id)
        serializer = DataSerializer(data, many=True)
        return Response(serializer.data, status.HTTP_200_OK)
