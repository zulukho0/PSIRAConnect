from django.db import models
from datetime import timedelta

# Create your models here.
class Course(models.Model):
    grade = models.CharField(max_length=10)  # Increased max_length to accommodate different grade formats
    description = models.CharField(max_length=255, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
            return self.grade

class SubjectTemplate(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='subjects')
    name = models.CharField(max_length=100)  # Subject name
    max_theory = models.IntegerField(default=100)
    max_practical = models.IntegerField(default=100)

    def __str__(self):
        return f"{self.course.grade} - {self.name}"