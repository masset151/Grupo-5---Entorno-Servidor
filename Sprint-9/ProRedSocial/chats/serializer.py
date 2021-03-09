from rest_framework import serializers
from chats.models import Chat
from usuario.serializer import UsuarioSerializer

class ChatSerializer(serializers.Serializer):
    id_chat = serializers.IntegerField()
    usuario = UsuarioSerializer(read_only=True)
    mensaje = serializers.CharField(max_length=200)
    class meta:
        model = Chat
        fields= '__all__'

    def create(self,validate_data):
        return Chat.objects.create(**validate_data)

    def update(self,instance,validate_data):
        instance.usuario = validate_data.get('usuario',instance.usuario)
        instance.mensaje = validate_data.get('mensaje',instance.mensaje)
        instance.save()
      
        return instance

