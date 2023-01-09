from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
# Create your models here.


class CustomUser(AbstractBaseUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_no = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    is_registered = models.BooleanField(default=0)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
