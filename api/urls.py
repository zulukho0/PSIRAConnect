from django.urls import path, include
from rest_framework import routers
from students.api_views import StudentViewSet
from courses.api_views import CourseViewSet
from classes.api_views import ClassViewSet
from results.api_views import ResultViewSet, ReportViewSet
from instructors.api_views import InstructorViewSet

router = routers.DefaultRouter()
router.register(r'students', StudentViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'classes', ClassViewSet)
router.register(r'results', ResultViewSet)
router.register(r'reports', ReportViewSet)
router.register(r'instructors', InstructorViewSet)

urlpatterns = [
    path('v1/', include(router.urls)),  # Prefix all endpoints with /api/v1/
]
