import os
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import File, FileData
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


class FileSerializer(serializers.ModelSerializer):

    ALLOWED_TYPES = [".xlsx", ".xls", ".csv"]

    class Meta:
        model = File
        fields = "__all__"

    def validate_file(self, value):
        file_extension = os.path.splitext(value.name)[1]
        if file_extension not in self.ALLOWED_TYPES:
            msg = "file accept only .xlsx, .xls, .csv"
            raise serializers.ValidationError(msg)
        return value


class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileData
        fields = "__all__"
