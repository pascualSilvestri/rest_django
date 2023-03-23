from rest_framework import serializers

from .models import Proyect

class ProjectSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Proyect
        fields =('id','titulo','descripcion','tecnologia','fecha')
        read_only_fields = ('fecha',)