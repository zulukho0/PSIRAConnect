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

class CourseCreateSerializer(serializers.ModelSerializer):
    subjects = SubjectTemplateSerializer(many=True, required=False)
    
    class Meta:
        model = Course
        fields = '__all__'
    
    def create(self, validated_data):
        subjects_data = validated_data.pop('subjects', [])
        course = Course.objects.create(**validated_data)
        
        for subject_data in subjects_data:
            SubjectTemplate.objects.create(course=course, **subject_data)
        
        return course