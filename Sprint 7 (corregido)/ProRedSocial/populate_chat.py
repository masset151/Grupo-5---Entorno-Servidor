import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'ProRedSocial.settings')

import django
django.setup()

import random
from faker import Faker
fakegen = Faker()

from publicacion.models import Publicacion
from usuario.models import Usuario
from chats.models import Chat

def populate(N=5):
    for entry in range(N):
        id = random.choice(range(Usuario.objects.count()))
        if(id==0):
            id = id+1
        num = Chat.objects.count()
        fake_id = num+1
        fake_mensaje = fakegen.text()
        fake_usuario = Usuario.objects.get(id_usuario=id)

        # Nueva entrada de Datos
        c = Chat.objects.get_or_create(id_chat=fake_id,usuario=fake_usuario,mensaje=fake_mensaje)[0]


if __name__ == '__main__':
    print("Rellenando Base de Datos")
    populate(1000)
    print("Completado")
