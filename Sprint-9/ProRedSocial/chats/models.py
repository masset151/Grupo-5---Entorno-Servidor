from django.db import models
from usuario.models import Usuario

# Create your models here.

class Chat(models.Model):
    id_chat = models.IntegerField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE,null=True)
    mensaje = models.CharField(max_length=250)

    def __int__(self):
        return self.id_chat
