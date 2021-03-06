from django.db import models

# Create your models here.
class Usuario(models.Model):
    id_usuario = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=128)
    apellido = models.CharField(max_length=128)
    email = models.EmailField(max_length=264, unique=True)
    contraseña = models.CharField(max_length=128)