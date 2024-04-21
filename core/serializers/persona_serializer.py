from rest_framework import serializers

from core.domain.persona.models import Persona
from core.serializers.vehiculo_serializer import VehiculoSerializer



class PersonaSerializer(serializers.ModelSerializer):
    Vehiculolist=VehiculoSerializer(many=True,read_only=True)
    class Meta:
        model=Persona
        #fields="__all__"
        exclude=['created','updated']