import math
from django.db import models
from students.models import Student
from classes.models import Class
from courses.models import SubjectTemplate
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
STATUS_CHOICES = [
    ('Pending', 'Pending'),
    ('Submitted', 'Submitted'),
]

class Result(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='results')
    class_instance = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='results')
    total_marks = models.IntegerField(default=0)
    average = models.IntegerField(default=0)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
    report_file = models.FileField(upload_to='reports/', null=True, blank=True)
    submitted_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.student} - {self.class_instance.course.grade} - {self.class_instance.batch_number}"

    def calculate_totals(self):
        subjects = self.subjects.all()
        if subjects.exists():
            total = sum([s.total_marks for s in subjects])
            self.total_marks = math.ceil(total)
            self.average = math.ceil(total / subjects.count())
        else:
            self.total_marks = 0
            self.average = 0
        self.save(update_fields=['total_marks', 'average'])

class SubjectResult(models.Model):
    result = models.ForeignKey(Result, on_delete=models.CASCADE, related_name='subjects')
    template = models.ForeignKey(SubjectTemplate, on_delete=models.CASCADE)
    theory_marks = models.IntegerField(default=0)
    practical_marks = models.IntegerField(default=0)
    total_marks = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        # Case 1: both theory and practical are provided
        if self.theory_marks is not None and self.practical_marks is not None:
            if self.theory_marks > 0 and self.practical_marks > 0:
                self.total_marks = math.ceil((self.theory_marks + self.practical_marks) / 2)
            elif self.theory_marks > 0:
                self.total_marks = math.ceil(self.theory_marks)
            elif self.practical_marks > 0:
                self.total_marks = math.ceil(self.practical_marks)
            else:
                self.total_marks = 0
        else:
            # default if both are None
            self.total_marks = 0

        super().save(*args, **kwargs)
        # Update parent result totals
        self.result.calculate_totals()


# Auto-create SubjectResults after a Result is created
@receiver(post_save, sender='results.Result')
def create_subjects_for_result(sender, instance, created, **kwargs):
    if created:
        templates = instance.class_instance.course.subjects.all()
        for template in templates:
            instance.subjects.create(template=template)

