import os
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import (
    SupplierQuantityFiles,
    SupplierQuantityFilesData,
    OutGoingQuantityFilesData,
    OutGoingQuantityFiles,
    OTDMFiles,
    OTDMFilesData,
    DINFiles,
    DINFilesData,
    NDVCTurnoverFiles,
    NDVCTurnoverFilesData,
    IndustrialEfficiencyFiles,
    IndustrialEfficiencyFilesData,
    NEEFiles,
    NEEFilesData,
)
from authentication.models import User


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        allow_null=False, validators=[UniqueValidator(queryset=User.objects.all())]
    )
    username = serializers.CharField(
        allow_null=False, validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(allow_null=False)
    first_name = serializers.CharField(allow_null=False)
    last_name = serializers.CharField(allow_null=False)
    phone_number = serializers.RegexField("[0-9]{10}")

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "first_name",
            "last_name",
            "project_name",
            "address",
            "phone_number",
            "comments",
            "unique_id",
            "id",
            "role",
            "password",
        ]


class UpdateUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        allow_null=False, validators=[UniqueValidator(queryset=User.objects.all())]
    )
    first_name = serializers.CharField(allow_null=False)
    last_name = serializers.CharField(allow_null=False)
    phone_number = serializers.RegexField("[0-9]{10}")

    class Meta:
        model = User
        fields = [
            "email",
            "first_name",
            "last_name",
            "project_name",
            "address",
            "phone_number",
            "comments",
        ]


class OutGoingQuantityFileSerializer(serializers.ModelSerializer):

    ALLOWED_TYPES = [".xlsx", ".xls"]

    class Meta:
        model = OutGoingQuantityFiles
        fields = "__all__"

    def validate_file(self, value):
        file_extension = os.path.splitext(value.name)[1]
        if file_extension not in self.ALLOWED_TYPES:
            msg = "file accept only .xlsx, .xls"
            raise serializers.ValidationError(msg)
        return value


class OutGoingQuantityDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = OutGoingQuantityFilesData
        fields = "__all__"


class SupplierQuantityFileSerializer(serializers.ModelSerializer):

    ALLOWED_TYPES = [".xlsx", ".xls"]

    class Meta:
        model = SupplierQuantityFiles
        fields = "__all__"

    def validate_file(self, value):
        file_extension = os.path.splitext(value.name)[1]
        if file_extension not in self.ALLOWED_TYPES:
            msg = "file accept only .xlsx, .xls"
            raise serializers.ValidationError(msg)
        return value


class SupplierQuantityDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupplierQuantityFilesData
        fields = "__all__"


class OTDMFilesSerializer(serializers.ModelSerializer):

    ALLOWED_TYPES = [".xlsx", ".xls"]

    class Meta:
        model = OTDMFiles
        fields = "__all__"

    def validate_file(self, value):
        file_extension = os.path.splitext(value.name)[1]
        if file_extension not in self.ALLOWED_TYPES:
            msg = "file accept only .xlsx, .xls"
            raise serializers.ValidationError(msg)
        return value


class OTDMFilesDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = OTDMFilesData
        fields = "__all__"


class DINFilesSerializer(serializers.ModelSerializer):

    ALLOWED_TYPES = [".xlsx", ".xls"]

    class Meta:
        model = DINFiles
        fields = "__all__"

    def validate_file(self, value):
        file_extension = os.path.splitext(value.name)[1]
        if file_extension not in self.ALLOWED_TYPES:
            msg = "file accept only .xlsx, .xls"
            raise serializers.ValidationError(msg)
        return value


class DINFilesDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = DINFilesData
        fields = "__all__"


class NDVCTurnoverFilesSerializer(serializers.ModelSerializer):

    ALLOWED_TYPES = [".xlsx", ".xls"]

    class Meta:
        model = NDVCTurnoverFiles
        fields = "__all__"

    def validate_file(self, value):
        file_extension = os.path.splitext(value.name)[1]
        if file_extension not in self.ALLOWED_TYPES:
            msg = "file accept only .xlsx, .xls"
            raise serializers.ValidationError(msg)
        return value


class NDVCTurnoverFilesDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = NDVCTurnoverFilesData
        fields = "__all__"


class IndustrialEfficiencyFilesSerializer(serializers.ModelSerializer):

    ALLOWED_TYPES = [".xlsx", ".xls"]

    class Meta:
        model = IndustrialEfficiencyFiles
        fields = "__all__"

    def validate_file(self, value):
        file_extension = os.path.splitext(value.name)[1]
        if file_extension not in self.ALLOWED_TYPES:
            msg = "file accept only .xlsx, .xls"
            raise serializers.ValidationError(msg)
        return value


class IndustrialEfficiencyFilesDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = IndustrialEfficiencyFilesData
        fields = "__all__"


class NEEFilesSerializer(serializers.ModelSerializer):

    ALLOWED_TYPES = [".xlsx", ".xls"]

    class Meta:
        model = NEEFiles
        fields = "__all__"

    def validate_file(self, value):
        file_extension = os.path.splitext(value.name)[1]
        if file_extension not in self.ALLOWED_TYPES:
            msg = "file accept only .xlsx, .xls"
            raise serializers.ValidationError(msg)
        return value


class NEEFilesDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = NEEFilesData
        fields = "__all__"
