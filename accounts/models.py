from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, UserManager
# Create your models here.


class CustomUser(AbstractBaseUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_no = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    is_registered = models.BooleanField(default=0)
    is_verified = models.BooleanField(default=0)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class UserDetails(models.Model):
    description = models.TextField()
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    county = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
