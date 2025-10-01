from django.urls import path
from . import views

urlpatterns = [
    path('student-report/<int:result_id>/', views.student_report, name='student_report'),
]
