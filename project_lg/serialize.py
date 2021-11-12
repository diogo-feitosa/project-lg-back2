from rest_framework import serializers
from project_lg.models import Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'name', 'startDate','endDate','value','risk']