from django.db import models
from courses.models import Course
from students.models import Student

# Create your models here.
class Class(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    course_number = models.CharField(max_length=50, null=True, blank=True)
    batch_number = models.CharField(max_length=20, unique=True, blank=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True)
    students = models.ManyToManyField(Student, related_name='classes')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        # Auto-set end_date to 5 days after start_date if not provided
        if not self.end_date and self.start_date:
            self.end_date = self.start_date + timedelta(days=4)

         # Auto-generate batch_number if not set
        if not self.batch_number:
            random_code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
            self.batch_number = f"{self.course.grade}-{random_code}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.course.grade} - {self.batch_number or 'Batch'} ({self.start_date} to {self.end_date})"
