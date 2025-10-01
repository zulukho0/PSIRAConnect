from rest_framework import viewsets
from students.models import Student
from .serializers import StudentSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filterset_fields = ['first_name', 'last_name', 'id_number']
    search_fields = ['first_name', 'last_name', 'id_number']
