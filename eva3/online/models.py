from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Consultas(models.Model):
    codigoConsulta = models.AutoField(primary_key=True)
    codigoRespuesta= models.AutoField(max_lenght=5)
    nombreCliente = models.CharField(max_length=35)
    consulta = models.CharField(max_length=500)

class Usuario(models.Model):
    usuario = models.CharField(max_length=20)
    contrasena = models.CharField(max_length=20)
    tipo = models.IntegerField