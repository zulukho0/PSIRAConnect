from rest_framework import serializers
from .models import Course, SubjectTemplate

class SubjectTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubjectTemplate
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    subjects = SubjectTemplateSerializer(many=True, read_only=True)
    class Meta:
        model = Course
        fields = '__all__'
