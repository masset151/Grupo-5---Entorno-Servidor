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
        fake_usuario = Usuario.objects.get(id_usuario=id_usuarioc)
        fake_historia =Historia.objects.get(id_historia=id_historiac)

        # Nueva entrada de Datos
        consultar = VerHistoria.objects.get_or_create(usuario=fake_usuario,historia=fake_historia)[0]


if __name__ == '__main__':
    print("Rellenando Base de Datos")
    populate(10)
    print("Completado")
