from unittest.util import _MAX_LENGTH
from django.db import models


# Create your models here.

class Consultas(models.Model):
    codigoConsulta = models.AutoField(primary_key=True)
    codigoRespuesta= models.ForeignKey("Usuario", verbose_name=("int"))
    nombreCliente = models.CharField(max_length=35)
    consulta = models.CharField(max_length=500)

class Respuesta(models.Model):
    codigoConsulta = models.ForeignKey("Consultas", verbose_name=("int"))
    codigoRespuesta = models.AutoField(primary_key=True)
    nombreTecnico = models.CharField(max_length=35)
    respuesta = models.CharField(max_length=500)