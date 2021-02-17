import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'ProRedSocial.settings')





import django
django.setup()

import random
from faker import Faker
fakegen = Faker()

from publicacion.models import Historia,VerHistoria
from usuario.models import Usuario

def populate(N=5):
    for entry in range(N):
        id_usuarioc = random.choice(range(Usuario.objects.count()))
        id_historiac = random.choice(range(Historia.objects.count()))

        if (id_usuarioc==0):
            id_usuarioc = id_usuarioc+1


        if (id_historiac==0):
            id_historiac = id_historiac+1
        

        print(id_usuarioc)
        fake_usuario = Usuario.objects.get(id_usuario=id_usuarioc)
        fake_historia =Historia.objects.get(id_historia=id_historiac)

        # Nueva entrada de Datos
        consultar = VerHistoria.objects.get_or_create(usuario=fake_usuario,historia=fake_historia)[0]


if __name__ == '__main__':
    print("Rellenando Base de Datos")
    populate(1000)
    print("Completado")
