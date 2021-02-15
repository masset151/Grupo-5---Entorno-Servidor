from django.db import models
from usuario.models import Usuario
from publicacion.models import Historia
from chats.models import Chat

# Create your models here.

class Cabecera(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    historia = models.ForeignKey(Historia, on_delete=models.CASCADE)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)