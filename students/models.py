from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50)
    id_number = models.CharField(max_length=13, unique=True)
    contact_number = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.id_number})"