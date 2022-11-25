from django.db import models

# Create your models here.
class TecnicoMaster(models.Model):
    usuarioTecnico = models.CharField(primary_key=True, max_length=20)
    nombreTecnico = models.CharField(max_length=20)

class Usuario(models.Model):
    usuarioUsuario = models.CharField(primary_key=True, max_length=20)
    nombreUsuario = models.CharField(max_length=20)