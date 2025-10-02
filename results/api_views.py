from rest_framework import viewsets
from results.models import Result
from .serializers import ResultSerializer
from users.permissions import RolePermission

class ResultViewSet(viewsets.ModelViewSet):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer
    permission_classes = [RolePermission]
    filterset_fields = ['student', 'class_instance', 'status']
