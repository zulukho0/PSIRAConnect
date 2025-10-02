from rest_framework import viewsets
from courses.models import Course
from .serializers import CourseSerializer
from users.permissions import RolePermission

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [RolePermission]
