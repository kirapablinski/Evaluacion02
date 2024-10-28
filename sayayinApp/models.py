from django.db import models

# Create your models here.
class Sayayin(models.Model):
    nombre = models.CharField(max_length=50)
    nivelfuerza = models.FloatField(max_length=50)
    vecesresuciado = models.FloatField(max_length=3)
    torneosgandos = models.FloatField(max_length=2)
    edad = models.FloatField(max_length=3)
    maestro = models.CharField(max_length=50)
    transformacionmax = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
