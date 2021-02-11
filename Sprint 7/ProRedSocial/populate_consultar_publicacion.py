import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'ProRedSocial.settings')





import django
django.setup()

import random
from faker import Faker
fakegen = Faker()

from publicacion.models import Publicacion,ConsultarPublicacion
from usuario.models import Usuario

def populate(N=5):
    for entry in range(N):
        id_usuarioc = random.choice(range(Usuario.objects.count()))
        id_publicacionc = random.choice(range(Publicacion.objects.count()))
        fake_usuario =Usuario.objects.get(id_usuario=id_usuarioc)
        fake_publicacion = Publicacion.objects.get(id_publicacion=id_publicacionc)

        # Nueva entrada de Datos
        consultarP = ConsultarPublicacion.objects.get_or_create(usuario=fake_usuario,publicacion=fake_publicacion)[0]


if __name__ == '__main__':
    print("Rellenando Base de Datos")
    populate(5)
    print("Completado")
