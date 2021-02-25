from rest_framework import serializers
from publicacion.models import Publicacion,Historia
from usuario.serializer import UsuarioSerializer

class PublicacionSerializer(serializers.Serializer):
    id_publicacion = serializers.IntegerField()
    fecha = serializers.DateField()
    hora = serializers.DateTimeField()
    lugar = serializers.CharField(max_length=300)
    usuario = UsuarioSerializer(read_only=True)
    archivo = serializers.URLField()
    class meta:
        model = Publicacion
        fields=['id_publicacion','fecha','hora','lugar','usuario','archivo']

    def create(self,validate_data):
        return Publicacion.objects.create(**validate_data)

    def update(self,instance,validate_data):
        instance.fecha = validate_data.get('fecha',instance.fecha)
        instance.hora = validate_data.get('hora',instance.hora)
        instance.lugar = validate_data.get('lugar',instance.lugar)
        instance.usuario = validate_data.get('usuario',instance.usuario)
        instance.archivo = validate_data.get('archivo',instance.archivo)
        instance.save()
      
        return instance

class HistoriaSerializer(serializers.Serializer):
    id_historia = serializers.IntegerField()
    usuario = UsuarioSerializer(read_only=True)
    archivo = serializers.URLField()
    class meta:
        model = Historia
        fields=['id_historia','usuario','archivo']

    def create(self,validate_data):
        return Historia.objects.create(**validate_data)

    def update(self,instance,validate_data):
        instance.usuario = validate_data.get('usuario',instance.usuario)
        instance.archivo = validate_data.get('archivo',instance.archivo)
        instance.save()
      
        return instance