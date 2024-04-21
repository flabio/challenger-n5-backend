from django.db import models

from core.domain.persona.models import Persona



# Create your models here.
class Vehiculo(models.Model):
    placa=models.CharField(max_length=50,unique=True)
    marca=models.CharField(max_length=50)
    color=models.CharField(max_length=50)
    persona=models.ForeignKey(Persona,on_delete=models.CASCADE,related_name="Vehiculolist")
    isActive=models.BooleanField(default=True)
    created     =   models.DateTimeField(auto_now_add=True)
    updated     =   models.DateTimeField(auto_now=True)
    
    def __str__(self)->str:
        return self.placa