from rest_framework import viewsets
from students.models import Student
from .serializers import StudentSerializer
from users.permissions import RolePermission


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [RolePermission]
    filterset_fields = ['first_name', 'last_name', 'id_number']
    search_fields = ['first_name', 'last_name', 'id_number']
