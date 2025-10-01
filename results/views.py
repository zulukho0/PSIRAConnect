from django.shortcuts import render, get_object_or_404
from .models import Result
from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML
import tempfile

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

def generate_result_pdf(request, result_id):
    result = get_object_or_404(Result, id=result_id)
    subjects = result.subjects.all()

    # Render HTML template
    html_string = render_to_string('results/result_report.html', {
        'result': result,
        'subjects': subjects,
    })

    # Generate PDF
    response = HttpResponse(content_type="application/pdf")
    response['Content-Disposition'] = f'filename=Result_{result.student.id}_{result.class_instance.id}.pdf'

    # Create PDF
    with tempfile.NamedTemporaryFile(delete=True) as tmp:
        HTML(string=html_string).write_pdf(target=response)

    return response
