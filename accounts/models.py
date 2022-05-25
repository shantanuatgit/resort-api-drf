from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    is_manager = models.BooleanField(default=False)
