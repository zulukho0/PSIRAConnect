from django.db import models
from students.models import Student
from classes.models import Class
from courses.models import SubjectTemplate

# Create your models here.
STATUS_CHOICES = [
    ('Pending', 'Pending'),
    ('Submitted', 'Submitted'),
]

class Result(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='results')
    class_instance = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='results')
    total_marks = models.IntegerField(default=0)
    average = models.FloatField(default=0.0)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
    report_file = models.FileField(upload_to='reports/', null=True, blank=True)
    submitted_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.student} - {self.class_instance.course.grade} - {self.class_instance.batch_number}"

    def calculate_totals(self):
        subjects = self.subjects.all()
        total = sum([s.total_marks for s in subjects])
        self.total_marks = total
        self.average = total / len(subjects) if subjects else 0
        self.save()

class SubjectResult(models.Model):
    result = models.ForeignKey(Result, on_delete=models.CASCADE, related_name='subjects')
    template = models.ForeignKey(SubjectTemplate, on_delete=models.CASCADE)
    theory_marks = models.IntegerField(default=0)
    practical_marks = models.IntegerField(default=0)
    total_marks = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        # Auto-calculate total marks
        self.total_marks = self.theory_marks + self.practical_marks
        super().save(*args, **kwargs)
        # Update parent Result totals and average
        self.result.calculate_totals()

    def __str__(self):
        return f"{self.result.student} - {self.template.name}"
