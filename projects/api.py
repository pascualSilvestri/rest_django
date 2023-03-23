from rest_framework import viewsets, permissions
from .models import Proyect
from .serializers import ProjectSerializer

class ProjectViewset(viewsets.ModelViewSet):
    queryset = Proyect.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProjectSerializer