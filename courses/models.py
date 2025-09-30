from django.db import models
from datetime import timedelta

# Create your models here.
class Course(models.Model):
    grade = models.CharField(max_length=1)
    description = models.CharField(max_length=255, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    start_date = models.DateField()
    end_date = models.DateField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Make sure Course duration is not > 5
    def save(self, *args, **kwargs):
            if not self.end_date and self.start_date:
                self.end_date = self.start_date + timedelta(days=4)  # 5-day course
            super().save(*args, **kwargs)

    def __str__(self):
            return self.grade