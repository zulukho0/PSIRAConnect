from django.urls import path
from . import views

urlpatterns = [
    path('student-report/<int:result_id>/', views.student_report, name='student_report'),
    path('report/<int:result_id>/', views.generate_result_pdf, name='generate_result_pdf'),
]
