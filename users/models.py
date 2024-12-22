from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # Add any additional fields you want
    # username, password, and email are already included from AbstractUser
    pass