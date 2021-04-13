from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from authentication.models import User


class UserSerializer(serializers.ModelSerializer):
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
            "first_name",
            "last_name",
            "project_name",
            "address",
            "phone_number",
            "comments",
            "unique_id",
            "id",
            "role",
            "password"
        ]
