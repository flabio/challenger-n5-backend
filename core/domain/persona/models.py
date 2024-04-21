from django.db import models

# Create your models here.
class Persona(models.Model):
    name        =   models.CharField(max_length=150)
    email       =   models.CharField(max_length=150,unique=True)
    isActive    =   models.BooleanField(default=True)
    created     =   models.DateTimeField(auto_now_add=True)
    updated     =   models.DateTimeField(auto_now=True)
    
    def __str__(self)->str:
        return self.name