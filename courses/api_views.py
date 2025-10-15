from rest_framework import viewsets
from rest_framework.response import Response
from courses.models import Course, SubjectTemplate
from .serializers import CourseSerializer, SubjectTemplateSerializer, CourseCreateSerializer
from users.permissions import RolePermission

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [RolePermission]
    
    def get_serializer_class(self):
        if self.action == 'create':
            return CourseCreateSerializer
        return CourseSerializer

class SubjectTemplateViewSet(viewsets.ModelViewSet):
    queryset = SubjectTemplate.objects.all()
    serializer_class = SubjectTemplateSerializer
    permission_classes = [RolePermission]