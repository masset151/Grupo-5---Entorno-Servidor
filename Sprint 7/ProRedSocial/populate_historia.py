import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'ProRedSocial.settings')





import django
django.setup()

import random
from faker import Faker
fakegen = Faker()

from publicacion.models import Historia
from usuario.models import Usuario

def populate(N=5):
    for entry in range(N):
        id = id = random.choice(range(Usuario.objects.count()))
        num = Historia.objects.count()
        fake_id = num+1
        fake_usuario = Usuario.objects.get(id_usuario=id)
        fake_archivo = fakegen.image_url(750,1334)

        # Nueva entrada de Datos
        historia = Historia.objects.get_or_create(id_historia=fake_id,usuario=fake_usuario,archivo=fake_archivo)[0]


if __name__ == '__main__':
    print("Rellenando Base de Datos")
    populate(10)
    print("Completado")
