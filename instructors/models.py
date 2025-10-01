from django.db import models

# Create your models here.
class Instructor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    psira_number = models.CharField(max_length=20, unique=True)
    signature = models.ImageField(upload_to='signatures/', null=True, blank=True)
    contact_number = models.CharField(max_length=15, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.psira_number})"