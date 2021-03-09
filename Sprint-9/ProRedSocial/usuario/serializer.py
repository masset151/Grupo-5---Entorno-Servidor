from rest_framework import serializers
from usuario.models import Usuario
class UsuarioSerializer(serializers.Serializer):
    id_usuario = serializers.IntegerField()
    nombre = serializers.CharField(max_length=128)
    apellido = serializers.CharField(max_length=128)
    email = serializers.EmailField(min_length=None,max_length=None,allow_blank=False)
    contraseña = serializers.CharField(max_length=128)
    nick = serializers.CharField(max_length=100)
    class meta:
        model = Usuario
        fields = "__all__"
       

    def create(self,validate_data):
        return Usuario.objects.create(**validate_data)

    def update(self,instance,validate_data):
        instance.nombre = validate_data.get('usuario',instance.nombre)
        instance.apellido = validate_data.get('apellido',instance.apellido)
        instance.email = validate_data.get('email',instance.email)
        instance.contaraseña = validate_data.get('contraseña',instance.contraseña)
        instance.nick = validate_data.get('nick', instance.nick)
        instance.save()
      
        return instance




