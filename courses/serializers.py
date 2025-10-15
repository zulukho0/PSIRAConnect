from rest_framework import serializers
from .models import Course, SubjectTemplate
import logging

logger = logging.getLogger(__name__)

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
        extra_kwargs = {
            'grade': {'max_length': 10}
        }
    
    def validate_grade(self, value):
        """
        Validate the grade field to ensure it's not empty and meets requirements
        """
        if not value or not value.strip():
            raise serializers.ValidationError("Grade cannot be empty")
        return value.strip()
    
    def create(self, validated_data):
        subjects_data = validated_data.pop('subjects', [])
        logger.info(f"Creating course with data: {validated_data}")
        logger.info(f"Creating subjects with data: {subjects_data}")
        
        try:
            course = Course.objects.create(**validated_data)
            
            for subject_data in subjects_data:
                SubjectTemplate.objects.create(course=course, **subject_data)
            
            return course
        except Exception as e:
            logger.error(f"Error creating course: {str(e)}")
            raise