from django.db import models
from students.models import Student
from classes.models import Class
from courses.models import SubjectTemplate
from django.db.models.signals import post_save
from django.dispatch import receiver
from decimal import Decimal, ROUND_HALF_UP
from django.template.loader import render_to_string
from weasyprint import HTML
import os
from django.conf import settings

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
        total = sum([s.total_marks for s in subjects])
        self.total_marks = total

        if subjects.exists():
            avg = Decimal(str(total)) / Decimal(str(subjects.count()))
            self.average = int(avg.to_integral_value(rounding=ROUND_HALF_UP))
        else:
            self.average = 0

        # Only save totals/average, do not generate PDF here
        self.save(update_fields=['total_marks', 'average'])

    def generate_pdf(self):
        # Render HTML template
        html_string = render_to_string('results/report_template.html', {'result': self})

        # Make sure the directory exists
        reports_dir = os.path.join(settings.MEDIA_ROOT, 'reports')
        os.makedirs(reports_dir, exist_ok=True)  # <-- creates folder if missing

        # PDF filename
        file_name = f'result_{self.id}.pdf'
        full_path = os.path.join(reports_dir, file_name)

        # Generate PDF
        HTML(string=html_string).write_pdf(target=full_path)

        # Save path to model
        self.report_file.name = f'reports/{file_name}'
        self.save(update_fields=['report_file'])


class SubjectResult(models.Model):
    result = models.ForeignKey(Result, on_delete=models.CASCADE, related_name='subjects')
    template = models.ForeignKey(SubjectTemplate, on_delete=models.CASCADE)
    theory_marks = models.FloatField(default=0.0, null=True, blank=True)
    practical_marks = models.FloatField(default=0.0, null=True, blank=True)
    total_marks = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        theory = Decimal(str(self.theory_marks)) if self.theory_marks is not None else None
        practical = Decimal(str(self.practical_marks)) if self.practical_marks is not None else None

        if theory and practical:
            if theory > 0 and practical > 0:
                self.total_marks = int(((theory + practical) / 2).to_integral_value(rounding=ROUND_HALF_UP))
            elif theory > 0:
                self.total_marks = int(theory.to_integral_value(rounding=ROUND_HALF_UP))
            elif practical > 0:
                self.total_marks = int(practical.to_integral_value(rounding=ROUND_HALF_UP))
            else:
                self.total_marks = 0
        elif theory:
            self.total_marks = int(theory.to_integral_value(rounding=ROUND_HALF_UP))
        elif practical:
            self.total_marks = int(practical.to_integral_value(rounding=ROUND_HALF_UP))
        else:
            self.total_marks = 0

        super().save(*args, **kwargs)
        # Update totals & average, but do NOT generate PDF here
        self.result.calculate_totals()


# Auto-create SubjectResults after a Result is created
@receiver(post_save, sender=Result)
def create_subjects_for_result(sender, instance, created, **kwargs):
    if created:
        templates = instance.class_instance.course.subjects.all()
        for template in templates:
            instance.subjects.create(template=template)
