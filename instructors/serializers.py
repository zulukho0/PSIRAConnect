from rest_framework import serializers
from .models import Instructor

class InstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instructor
        fields = ['id', 'first_name', 'last_name', 'psira_number', 'contact_number', 'signature']
