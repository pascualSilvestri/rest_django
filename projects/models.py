from django.db import models


class Proyect(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    tecnologia = models.CharField(max_length=200)
    fecha = models.DateTimeField(auto_now_add=True)