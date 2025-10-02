from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from students.models import Student
from .serializers import StudentSerializer
from users.permissions import RolePermission


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [RolePermission]
    filterset_fields = ['first_name', 'last_name', 'id_number']
    search_fields = ['first_name', 'last_name', 'id_number']

    @action(detail=False, methods=['get'], permission_classes=[])
    def debug_auth(self, request):
        """Debug endpoint to check authentication"""
        return Response({
            'user': str(request.user),
            'is_authenticated': request.user.is_authenticated,
            'role': getattr(request.user, 'role', 'NO ROLE ATTRIBUTE'),
            'is_staff': getattr(request.user, 'is_staff', False),
            'is_superuser': getattr(request.user, 'is_superuser', False),
        })
