from rest_framework import serializers
from .models import Result, SubjectResult

class SubjectResultSerializer(serializers.ModelSerializer):
    template_name = serializers.CharField(source='template.name', read_only=True)

    class Meta:
        model = SubjectResult
        fields = '__all__'

class ResultSerializer(serializers.ModelSerializer):
    subjects = SubjectResultSerializer(many=True, read_only=True)
    student_name = serializers.CharField(source='student.first_name', read_only=True)

    class Meta:
        model = Result
        fields = '__all__'
