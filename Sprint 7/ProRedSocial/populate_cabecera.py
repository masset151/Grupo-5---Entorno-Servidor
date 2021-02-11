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
        id_usuariof = random.choice(range(Usuario.objects.count()))-1
        id_chatf = random.choice(range(Chat.objects.count()))-1
        id_historiaf = random.choice(range(Historia.objects.count()))-1
       
        fake_usuario = Usuario.objects.get(id_usuario=id_usuariof)
        fake_historia =Historia.objects.get(id_historia=id_historiaf)
        fake_chat = Chat.objects.get(id_chat=id_chatf)

        # Nueva entrada de Datos
        cabecera = Cabecera.objects.get_or_create(usuario=fake_usuario,historia=fake_historia,chat=fake_chat)[0]


if __name__ == '__main__':
    print("Rellenando Base de Datos")
    populate(10)
    print("Completado")
