from django.db import models

from core.domain.vehiculo.models import Vehiculo

# Create your models here.
class Infraccion(models.Model):
    placa_patente=models.ForeignKey(Vehiculo,on_delete=models.CASCADE,related_name="infraccionlist")
    time_infringement=models.DateTimeField(auto_created=False)
    comment=models.TextField()
    
    def __str__(self)->str:
        return self.comment
    