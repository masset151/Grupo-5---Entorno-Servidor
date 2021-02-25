from rest_framework import serializers
from cabecera.models import Cabecera
from usuario.serializer import UsuarioSerializer
from chats.serializer import ChatSerializer
from publicacion.serializer import HistoriaSerializer

class CabeceraSerializer(serializers.Serializer):
    usuario = UsuarioSerializer(read_only=True)
    historia = HistoriaSerializer(read_only=True)
    chat = ChatSerializer(read_only=True)
    class meta:
        model = Cabecera
        fields= '__all__'

    def create(self,validate_data):
        return Cabecera.objects.create(**validate_data)

    def update(self,instance,validate_data):
        instance.usuario = validate_data.get('usuario',instance.usuario)
        instance.historia = validate_data.get('historia',instance.historia)
        instance.chat = validate_data.get('chat',instance.chat)
        instance.save()
      
        return instance

