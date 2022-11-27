from unittest.util import _MAX_LENGTH
from django.db import models


# Create your models here.

class Consultas(models.Model):
    codigoConsulta = models.AutoField(primary_key=True)
    #codigoRespuesta= models.ForeignKey("Usuario", models.DO_NOTHING, verbose_name=("int"))
    nombreCliente = models.CharField(max_length=35)
    consulta = models.CharField(max_length=500)

class Respuesta(models.Model):
    #codigoConsulta = models.ForeignKey("Consultas", models.DO_NOTHING, verbose_name=("int"))
    codigoRespuesta = models.AutoField(primary_key=True)
    nombreTecnico = models.CharField(max_length=35)
    respuesta = models.CharField(max_length=500)