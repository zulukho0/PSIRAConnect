from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('ADMIN', 'Admin'),
        ('MANAGER', 'Manager'),
        ('LECTURER', 'Lecturer'),
        ('CLERK', 'Clerk'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='CLERK')

    def __str__(self):
        return f"{self.username} ({self.role})"