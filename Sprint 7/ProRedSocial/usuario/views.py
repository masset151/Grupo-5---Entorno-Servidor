from django.shortcuts import render
from django.http import HttpResponse
from usuario.models import Usuario

# Create your views here.
def usuario(request):
    users_list = Usuario.objects.order_by("id_usuario")
    usuarios_dict = {'usuarios': users_list}

    return render(request, 'usuario/Usuario.html', context=usuarios_dict)