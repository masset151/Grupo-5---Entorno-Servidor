import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'ProRedSocial.settings')





import django
django.setup()

import random
from faker import Faker
fakegen = Faker()

from publicacion.models import Publicacion
from usuario.models import Usuario

def populate(N=5):
    for entry in range(N):
        id = random.choice(range(Usuario.objects.count()))
        num = Publicacion.objects.count()
        fake_id = num+1
        fake_lugar = fakegen.city()
        fake_usuario = Usuario.objects.get(id_usuario=id)
        fake_archivo = fakegen.image_url(600,400)

        # Nueva entrada de Datos
        publicacion = Publicacion.objects.get_or_create(id_publicacion=fake_id, lugar=fake_lugar, usuario=fake_usuario, archivo=fake_archivo)[0]


if __name__ == '__main__':
    print("Rellenando Base de Datos")
    populate(10)
    print("Completado")
