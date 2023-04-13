from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class Admin(User):
    is_superadmin = models.BooleanField(default=False)

class Professor(User):
    department = models.CharField(max_length=50)
    office_hours = models.CharField(max_length=50)

class Student(User):
    major = models.CharField(max_length=50)
    year = models.IntegerField()