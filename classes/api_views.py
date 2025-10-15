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

    @action(detail=True, methods=['post'], url_path='add_student')
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
        
        # Return the updated class including all students
        serializer = ClassSerializer(class_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'], url_path='remove_student')
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
        
        # Return the updated class including all students
        serializer = ClassSerializer(class_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'], url_path='update_students')
    def update_students(self, request, pk=None):
        class_instance = self.get_object()
        student_ids = request.data.get('students', [])

        # Validate all student IDs exist
        students = []
        for student_id in student_ids:
            try:
                student = Student.objects.get(id=student_id)
                students.append(student)
            except Student.DoesNotExist:
                return Response({"detail": f"Student with id {student_id} not found"}, status=status.HTTP_404_NOT_FOUND)
        
        # Update the students relationship
        class_instance.students.set(students)
        class_instance.save()
        
        # Return the updated class including all students
        serializer = ClassSerializer(class_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)