from rest_framework import serializers

from core.domain.infraccion.models import Infraccion


class InfraccionSerializer(serializers.ModelSerializer):
    placa=serializers.CharField(source='placa_patente.placa')
    class Meta:
        model=Infraccion
        fields="__all__"

class InfraccionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Infraccion
        fields="__all__"
