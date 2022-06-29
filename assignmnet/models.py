from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

from .managers import EmployeeUserManager

class EmployeeUser(AbstractBaseUser, PermissionsMixin):
   is_superuser = models.BooleanField(default=False)
   is_manager = models.BooleanField(default=False)
   is_employee =  models.BooleanField(default=False)
   is_active = models.BooleanField(default=True)
   is_staff = models.BooleanField(default=True)
   id = models.CharField(max_length=200, unique=True, primary_key=True)
   name = models.CharField(max_length=200)
   mob = models.CharField(max_length=15, unique=True)
   email = models.CharField(max_length=200, unique=True)
   role = models.CharField(max_length=200)

   USERNAME_FIELD = 'email'
   REQUIRED_FIELDS = []

   objects = EmployeeUserManager()

   def __str__(self):
      return self.email

