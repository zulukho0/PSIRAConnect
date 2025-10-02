from rest_framework import viewsets
from classes.models import Class
from .serializers import ClassSerializer
from users.permissions import RolePermission

class ClassViewSet(viewsets.ModelViewSet):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer
    permission_classes = [RolePermission]
