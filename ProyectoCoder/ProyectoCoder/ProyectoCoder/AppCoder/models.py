from django.db import models

# Create your models here.


class Familiar(models.Model):

    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    edad = models.IntegerField()


"""
DEFINIR SOLO LA CLASE FAMILIAR
class Familiar_2(models.Model):

    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    edad = models.DateField()


class Familiar_3(models.Model):

    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    edad = models.DateField()"""
