from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User


class LoginSerilizer(serializers.Serializer):
    username = serializers.CharField(max_length=250, required=True, allow_blank=False)
    password = serializers.CharField(max_length=250, required=True, allow_blank=False)

    # def validate_username(self,username):
    #     return self.get_auth_user(username)


class AuthorizationSerializer(serializers.Serializer):
    access_token = serializers.CharField(max_length=5000)
    refresh_token = serializers.CharField(max_length=5000)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username"]
        read_only_fields = ["id"]


class LoginResponseSerializer(serializers.Serializer):
    authorization = AuthorizationSerializer()
    user = UserSerializer


class SignupSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        allow_null=False, validators=[UniqueValidator(queryset=User.objects.all())]
    )
    username = serializers.CharField(
        allow_null=False, validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(
        allow_null=False
    )
    first_name = serializers.CharField(allow_null=False)
    last_name = serializers.CharField(allow_null=False)
    phone_number = serializers.RegexField("[0-9]{10}")

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password",
            "first_name",
            "last_name",
            "project_name",
            "address",
            "phone_number",
            "comments",
            "unique_id",
            "role"
        ]
