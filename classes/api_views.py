from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from classes.models import Class
from .serializers import ClassSerializer
from users.permissions import RolePermission
from students.models import Student

class ClassViewSet(viewsets.ModelViewSet):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer
    permission_classes = [RolePermission]


# Add a single student
    @action(detail=True, methods=['post'])
    def add_student(self, request, pk=None):
        class_instance = self.get_object()
        student_id = request.data.get('student_id')
        if not student_id:
            return Response({"detail": "student_id is required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            student = Student.objects.get(id=student_id)
        except Student.DoesNotExist:
            return Response({"detail": "Student not found"}, status=status.HTTP_404_NOT_FOUND)

        class_instance.students.add(student)
        class_instance.save()
        return Response({"detail": f"Student {student.first_name} added"}, status=status.HTTP_200_OK)

    # Remove a single student
    @action(detail=True, methods=['post'])
    def remove_student(self, request, pk=None):
        class_instance = self.get_object()
        student_id = request.data.get('student_id')
        if not student_id:
            return Response({"detail": "student_id is required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            student = Student.objects.get(id=student_id)
        except Student.DoesNotExist:
            return Response({"detail": "Student not found"}, status=status.HTTP_404_NOT_FOUND)

        class_instance.students.remove(student)
        class_instance.save()
        return Response({"detail": f"Student {student.first_name} removed"}, status=status.HTTP_200_OK)