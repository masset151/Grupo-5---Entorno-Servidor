from rest_framework import serializers
from AppRedSocial.models import User
from rest_framework.validators import UniqueValidator
import re
class UserSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=128)
    last_name = serializers.CharField(max_length=128)
    email = serializers.EmailField(min_length=None,max_length=None,allow_blank=False)
    nick =  serializers.CharField(max_length=32,required=True,validators=[UniqueValidator(queryset=User.objects.all())])

    class meta:
        model = User
        fields=['first_name','last_name','email','nick']

    def create(self,validate_data):
        return User.objects.create(**validate_data)

    def update(self,instance,validate_data):
        instance.first_name = validate_data.get('first_name',instance.first_name)
        instance.last_name = validate_data.get('last_name',instance.last_name)
        instance.email = validate_data.get('email',instance.email)
        instance.nick = validate_data.get('nick',instance.nick)
        instance.save()

        return instance




