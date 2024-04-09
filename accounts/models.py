from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    email = models.EmailField(unique=True)  # Add email field
    first_name = models.CharField(max_length=30)  # Add first name field
    last_name = models.CharField(max_length=30)  # Add last name field

    def __str__(self):
        return self.username