from rest_framework import serializers
from .models import Class
from students.serializers import StudentSerializer
from instructors.serializers import InstructorSerializer

class ClassSerializer(serializers.ModelSerializer):
    students = StudentSerializer(many=True, read_only=True)
    instructor = InstructorSerializer(read_only=True)

    class Meta:
        model = Class
        fields = '__all__'
