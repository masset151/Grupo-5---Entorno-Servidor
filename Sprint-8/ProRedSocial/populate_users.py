import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE",'ProRedSocial.settings')

import django
django.setup()

from usuario.models import Usuario
from faker import Faker


fakegen = Faker()

def populate(N=5):
    for entry in range(N):
        num = Usuario.objects.count()
        fake_id = num +1
        fake_name = fakegen.name().split()
        fake_nombre = fake_name[0]
        fake_apellido = fake_name[1]
        fake_email = fakegen.email()
        fake_password = fakegen.password()

        # Nueva entrada de Datos
        usuario = Usuario.objects.get_or_create(id_usuario=fake_id,nombre=fake_nombre,apellido = fake_apellido,email = fake_email,contraseña=fake_password)[0]

if __name__ == '__main__':
    print("Rellenando Base de Datos") 
    populate(10)
    print("Completado")