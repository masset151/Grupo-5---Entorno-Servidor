from django.db import models
from usuario.models import Usuario

# Create your models here.

class Publicacion(models.Model):
    id_publicacion = models.IntegerField(primary_key=True)
    fecha = models.DateField(auto_now_add=True)
    hora = models.DateTimeField(auto_now=True)
    lugar = models.CharField(max_length=300)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    archivo = models.URLField()
    def __int__(self):
        return self.id_publicacion

class ConsultarPublicacion(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    publicacion = models.ForeignKey(Publicacion, on_delete=models.CASCADE)

class Historia(models.Model):
    id_historia = models.IntegerField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    archivo = models.URLField()
    def __int__(self):
        return self.id_historia

class VerHistoria(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    historia = models.ForeignKey(Historia, on_delete=models.CASCADE)