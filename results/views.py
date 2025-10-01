from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Result

# Create your views here.
def student_report(request, result_id):
    result = get_object_or_404(Result, id=result_id)
    subject_results = result.subjects.all().order_by('template__name')

    context = {
        'result': result,
        'student': result.student,
        'class_instance': result.class_instance,
        'course': result.class_instance.course,
        'subject_results': subject_results,
    }
    return render(request, 'results/student_report.html', context)
