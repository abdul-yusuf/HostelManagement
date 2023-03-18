from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    is_worker = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    phone_no = models.CharField(max_length=20)
    room = models.ForeignKey('hostel.Room', on_delete=models.CASCADE, null=True)