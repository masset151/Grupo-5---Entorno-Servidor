import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'ProRedSocial.settings')





import django
django.setup()

import random
from faker import Faker
fakegen = Faker()

from cabecera.models import Cabecera
from publicacion.models import Historia
from usuario.models import Usuario
from chats.models import Chat


def populate(N=5):
    for entry in range(N):
        id_usuariof = random.choice(range(Usuario.objects.count()))
        #print(id_usuariof)
        if(id_usuariof==0):
            id_usuariof = id_usuariof+1
        id_chatf = random.choice(range(Chat.objects.count()))
        #print(id_chatf)
        if(id_chatf==0):
            id_chatf= id_chatf+1
        
        id_historiaf = random.choice(range(Historia.objects.count()))
        #print(id_historiaf)
        if(id_historiaf==0):
            id_historiaf= id_historiaf+1
       
        fake_usuario = Usuario.objects.get(id_usuario=id_usuariof)
        fake_historia =Historia.objects.get(id_historia=id_historiaf)
        fake_chat = Chat.objects.get(id_chat=id_chatf)

        # Nueva entrada de Datos
        cabecera = Cabecera.objects.get_or_create(usuario=fake_usuario,historia=fake_historia,chat=fake_chat)[0]


if __name__ == '__main__':
    print("Rellenando Base de Datos")
    populate(10)
    print("Completado")
