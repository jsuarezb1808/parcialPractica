from django.db import models

# Create your models here.
class Vuelos(models.Model):
    id=models.IntegerField()
    nombre = models.CharField(max_length=255)
    tipo = models.CharField(max_length=255)
    precio = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

