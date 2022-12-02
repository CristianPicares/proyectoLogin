from unittest.util import _MAX_LENGTH
from django.db import models


# Create your models here.

class Consultas(models.Model):
    codigoConsultaClien = models.AutoField(primary_key=True)
    codigoRespuestaClien = models.CharField(max_length=5, null=True)
    nombreCliente = models.CharField(max_length=35)
    consulta = models.CharField(max_length=500)

class Respuesta(models.Model):
    codigoConsultaTec = models.ForeignKey(Consultas, verbose_name=("Codigo Consulta"), on_delete=models.CASCADE)
    CodigoRespuestaTec = models.AutoField(primary_key=True)
    nombreTecnico = models.CharField(max_length=35)
    respuesta = models.CharField(max_length=500)
