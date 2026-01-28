from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLES = [
        ('admin', 'Administrador'),
        ('user', 'Usuario'),
    ]

    role = models.CharField(verbose_name='Rol', choices=ROLES, max_length=15, default='user')
