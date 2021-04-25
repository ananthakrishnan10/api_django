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

from .models import (
    OutGoingQuantityFilesData,
    OTDMFilesData,
    DINFilesData,
    NDVCTurnoverFilesData,
    IndustrialEfficiencyFilesData,
    NEEFilesData,
    SupplierQuantityFilesData,
)
from .serializer import (
    UserSerializer,
    UpdateUserSerializer,
    OutGoingQuantityFileSerializer,
    OutGoingQuantityDataSerializer,
    OTDMFilesSerializer,
    OTDMFilesDataSerializer,
    DINFilesSerializer,
    DINFilesDataSerializer,
    NDVCTurnoverFilesSerializer,
    NDVCTurnoverFilesDataSerializer,
    IndustrialEfficiencyFilesSerializer,
    IndustrialEfficiencyFilesDataSerializer,
    NEEFilesSerializer,
    NEEFilesDataSerializer,
    SupplierQuantityFileSerializer,
    SupplierQuantityDataSerializer,
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


class OutGoingQuantityView(CreateAPIView):
    # permission_classes = [IsAuthenticated, IsAdminAccessible]
    permission_classes = [AllowAny]
    serializer_class = OutGoingQuantityFileSerializer
    parser_classes = [MultiPartParser]

    def create(self, request, format=None):
        serializer = OutGoingQuantityFileSerializer(data=request.data)
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
                raise Exception("File Format not supported")
            serializers_data = []
            for index, row in df.iterrows():
                try:
                    input_data = {
                        "file_id": serializer.data["id"],
                        "month": row[0],
                        "assy_production_ppm": row[1],
                        "molding_production_ppm": row[2],
                        "month_actual": row[3],
                        "month_target": row[4],
                        "ytd_actual": row[5],
                        "ytd_target": row[6],
                    }
                    dataSerializer = OutGoingQuantityDataSerializer(data=input_data)
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


class OutGoingQuantityDataList(generics.ListAPIView):
    queryset = OutGoingQuantityFilesData.objects.order_by("-id")[:1]
    serializer_class = OutGoingQuantityDataSerializer
    # permission_classes = [IsAuthenticated, IsAdminAccessible]
    permission_classes = [AllowAny]

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = OutGoingQuantityDataSerializer(queryset, many=True)
        try:
            file_id = json.loads(json.dumps(serializer.data[0]))["file_id"]
        except:
            return Response({"message" : "No records found"}, status.HTTP_404_NOT_FOUND)
        data = OutGoingQuantityFilesData.objects.filter(file_id=file_id)
        serializer = OutGoingQuantityDataSerializer(data, many=True)
        return Response(serializer.data, status.HTTP_200_OK)


class SupplierQuantityView(CreateAPIView):
    # permission_classes = [IsAuthenticated, IsAdminAccessible]
    permission_classes = [AllowAny]
    serializer_class = SupplierQuantityFileSerializer
    parser_classes = [MultiPartParser]

    def create(self, request, format=None):
        serializer = SupplierQuantityFileSerializer(data=request.data)
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
                raise Exception("File Format not supported")
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
                    dataSerializer = SupplierQuantityDataSerializer(data=input_data)
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


class SupplierQuantityDataList(generics.ListAPIView):
    queryset = SupplierQuantityFilesData.objects.order_by("-id")[:1]
    serializer_class = SupplierQuantityDataSerializer
    # permission_classes = [IsAuthenticated, IsAdminAccessible]
    permission_classes = [AllowAny]

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = SupplierQuantityDataSerializer(queryset, many=True)
        try:
            file_id = json.loads(json.dumps(serializer.data[0]))["file_id"]
        except:
            return Response({"message" : "No records found"}, status.HTTP_404_NOT_FOUND)
        data = SupplierQuantityFilesData.objects.filter(file_id=file_id)
        serializer = SupplierQuantityDataSerializer(data, many=True)
        return Response(serializer.data, status.HTTP_200_OK)


class OTDMView(CreateAPIView):
    # permission_classes = [IsAuthenticated, IsAdminAccessible]
    permission_classes = [AllowAny]
    serializer_class = OTDMFilesSerializer
    parser_classes = [MultiPartParser]

    def create(self, request, format=None):
        serializer = OTDMFilesSerializer(data=request.data)
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
                raise Exception("File Format not supported")
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
                    dataSerializer = OTDMFilesDataSerializer(data=input_data)
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


class OTDMDataList(generics.ListAPIView):
    queryset = OTDMFilesData.objects.order_by("-id")[:1]
    serializer_class = OTDMFilesDataSerializer
    # permission_classes = [IsAuthenticated, IsAdminAccessible]
    permission_classes = [AllowAny]

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = OTDMFilesDataSerializer(queryset, many=True)
        try:
            file_id = json.loads(json.dumps(serializer.data[0]))["file_id"]
        except:
            return Response({"message" : "No records found"}, status.HTTP_404_NOT_FOUND)
        data = OTDMFilesData.objects.filter(file_id=file_id)
        serializer = OTDMFilesDataSerializer(data, many=True)
        return Response(serializer.data, status.HTTP_200_OK)


class DINView(CreateAPIView):
    # permission_classes = [IsAuthenticated, IsAdminAccessible]
    permission_classes = [AllowAny]
    serializer_class = DINFilesSerializer
    parser_classes = [MultiPartParser]

    def create(self, request, format=None):
        serializer = DINFilesSerializer(data=request.data)
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
                raise Exception("File Format not supported")
            serializers_data = []
            for index, row in df.iterrows():
                try:
                    input_data = {
                        "file_id": serializer.data["id"],
                        "month": row[0],
                        "actual_ytd_din": row[1],
                        "target_ytd_din": row[2],
                        "actual_spot_din": row[3],
                        "target_spot_din": row[4],
                        "net_inventorys": row[5],
                    }
                    dataSerializer = DINFilesDataSerializer(data=input_data)
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


class DINDataList(generics.ListAPIView):
    queryset = DINFilesData.objects.order_by("-id")[:1]
    serializer_class = DINFilesDataSerializer
    # permission_classes = [IsAuthenticated, IsAdminAccessible]
    permission_classes = [AllowAny]

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = DINFilesDataSerializer(queryset, many=True)
        try:
            file_id = json.loads(json.dumps(serializer.data[0]))["file_id"]
        except:
            return Response({"message" : "No records found"}, status.HTTP_404_NOT_FOUND)
        data = DINFilesData.objects.filter(file_id=file_id)
        serializer = DINFilesDataSerializer(data, many=True)
        return Response(serializer.data, status.HTTP_200_OK)


class NDVCTurnoverView(CreateAPIView):
    # permission_classes = [IsAuthenticated, IsAdminAccessible]
    permission_classes = [AllowAny]
    serializer_class = NDVCTurnoverFilesSerializer
    parser_classes = [MultiPartParser]

    def create(self, request, format=None):
        serializer = NDVCTurnoverFilesSerializer(data=request.data)
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
                raise Exception("File Format not supported")
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
                    dataSerializer = NDVCTurnoverFilesDataSerializer(data=input_data)
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


class NDVCTurnoverDataList(generics.ListAPIView):
    queryset = NDVCTurnoverFilesData.objects.order_by("-id")[:1]
    serializer_class = NDVCTurnoverFilesDataSerializer
    # permission_classes = [IsAuthenticated, IsAdminAccessible]
    permission_classes = [AllowAny]

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = NDVCTurnoverFilesDataSerializer(queryset, many=True)
        try:
            file_id = json.loads(json.dumps(serializer.data[0]))["file_id"]
        except:
            return Response({"message" : "No records found"}, status.HTTP_404_NOT_FOUND)
        data = NDVCTurnoverFilesData.objects.filter(file_id=file_id)
        serializer = NDVCTurnoverFilesDataSerializer(data, many=True)
        return Response(serializer.data, status.HTTP_200_OK)


class IndustrialEfficiencyView(CreateAPIView):
    # permission_classes = [IsAuthenticated, IsAdminAccessible]
    permission_classes = [AllowAny]
    serializer_class = IndustrialEfficiencyFilesSerializer
    parser_classes = [MultiPartParser]

    def create(self, request, format=None):
        serializer = IndustrialEfficiencyFilesSerializer(data=request.data)
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
                raise Exception("File Format not supported")
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
                    dataSerializer = IndustrialEfficiencyFilesDataSerializer(
                        data=input_data
                    )
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


class IndustrialEfficiencyDataList(generics.ListAPIView):
    queryset = IndustrialEfficiencyFilesData.objects.order_by("-id")[:1]
    serializer_class = IndustrialEfficiencyFilesDataSerializer
    # permission_classes = [IsAuthenticated, IsAdminAccessible]
    permission_classes = [AllowAny]

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = IndustrialEfficiencyFilesDataSerializer(queryset, many=True)
        try:
            file_id = json.loads(json.dumps(serializer.data[0]))["file_id"]
        except:
            return Response({"message" : "No records found"}, status.HTTP_404_NOT_FOUND)
        data = IndustrialEfficiencyFilesData.objects.filter(file_id=file_id)
        serializer = IndustrialEfficiencyFilesDataSerializer(data, many=True)
        return Response(serializer.data, status.HTTP_200_OK)


class NEEView(CreateAPIView):
    # permission_classes = [IsAuthenticated, IsAdminAccessible]
    permission_classes = [AllowAny]
    serializer_class = NEEFilesSerializer
    parser_classes = [MultiPartParser]

    def create(self, request, format=None):
        serializer = NEEFilesSerializer(data=request.data)
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
                raise Exception("File Format not supported")
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
                    dataSerializer = NEEFilesDataSerializer(data=input_data)
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


class NEEDataList(generics.ListAPIView):
    queryset = NEEFilesData.objects.order_by("-id")[:1]
    serializer_class = NEEFilesDataSerializer
    # permission_classes = [IsAuthenticated, IsAdminAccessible]
    permission_classes = [AllowAny]

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = NEEFilesDataSerializer(queryset, many=True)
        try:
            file_id = json.loads(json.dumps(serializer.data[0]))["file_id"]
        except:
            return Response({"message" : "No records found"}, status.HTTP_404_NOT_FOUND)
        data = NEEFilesData.objects.filter(file_id=file_id)
        serializer = NEEFilesDataSerializer(data, many=True)
        return Response(serializer.data, status.HTTP_200_OK)
