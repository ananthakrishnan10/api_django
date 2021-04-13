from django.contrib.auth.models import AbstractUser, Group
from django.db import models


# Create your models here.


class User(AbstractUser):
    role = models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
        related_name="user_role",
        null=True,
        blank=True,
    )
    password = models.CharField(max_length=20, null=False, blank=False)
    project_name = models.CharField(max_length=250, null=False)
    address = models.CharField(max_length=250, null=False)
    phone_number = models.CharField(max_length=250, null=False)
    comments = models.CharField(max_length=250, null=False)
    unique_id = models.CharField(max_length=250)

    def __str__(self):
        return self.email
