from rest_framework import serializers

from core.domain.vehiculo.models import Vehiculo
from core.serializers.infraccion_serializer import InfraccionSerializer


class VehiculoSerializer(serializers.ModelSerializer):
    infraccionlist=InfraccionSerializer(many=True, read_only=True)
    class Meta:
        model = Vehiculo
        #fields="__all__"
        exclude=['created','updated']
        
        