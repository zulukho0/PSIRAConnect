from django.db import models
from datetime import timedelta

# Create your models here.
class Course(models.Model):
    grade = models.CharField(max_length=1)
    description = models.CharField(max_length=255, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
            return self.grade