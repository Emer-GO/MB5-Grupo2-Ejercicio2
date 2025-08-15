from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    dni = models.CharField(max_length=20, unique=True)
    telefono = models.CharField(max_length=20)
