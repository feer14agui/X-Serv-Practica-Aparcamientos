from django.db import models

# Create your models here.
class Aparcamiento(models.Model):
	ident = models.CharField(max_length=32)
	Nombre = models.TextField()
	Nombre_via = models.CharField(max_length=32)
	Clase_vial = models.CharField(max_length=32)
	Numero = models.CharField(max_length=32)
	Localidad = models.CharField(max_length=32)
	Provincia = models.CharField(max_length=32)
	Cod_Postal = models.CharField(max_length=32)
	Barrio = models.CharField(max_length=32)
	Distrito = models.CharField(max_length=32)
	Coord_X = models.CharField(max_length=32)
	Coord_Y = models.CharField(max_length=32)
	Enlace = models.CharField(max_length=256)
	Descripcion = models.TextField()
	Accesibilidad = models.CharField(max_length=32)
	Telefono= models.CharField(max_length=15)
	Email = models.CharField(max_length=20)
	Num_Comentario = models.IntegerField(default=0)

class Usuario(models.Model):
	Nombre = models.CharField(max_length=32)
	Contraseña = models.CharField(max_length=32)
	Titulo_pagina = models.CharField(max_length=32)

class Comentario(models.Model):
	Aparcamiento = models.ForeignKey(Aparcamiento)
	Texto = models.TextField()

class Fecha(models.Model):
	Aparcamiento = models.ForeignKey(Aparcamiento)
	Usuario = models.ForeignKey(Usuario)
	Fecha = models.DateField()
