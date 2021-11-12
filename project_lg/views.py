from rest_framework import viewsets
from project_lg.models import Project
from project_lg.serialize import ProjectSerializer

class ProjectsViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class =  ProjectSerializer