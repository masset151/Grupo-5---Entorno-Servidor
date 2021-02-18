from django.shortcuts import render
from django.http import HttpResponse
from publicacion.models import Publicacion, ConsultarPublicacion, Historia, VerHistoria
from usuario.models import Usuario

# Create your views here.
def publicacion(request):
    pu_list = Publicacion.objects.order_by("id_publicacion")
    pu_dict = {'publicacion': pu_list}

    return render(request,'publicacion/publicacion.html', context=pu_dict)

def historia(request):
    his_list = Historia.objects.order_by("id_historia")
    his_dict = {'historia': his_list}

    return render(request, 'publicacion/historia.html', context=his_dict)

def chat(request):

    chat_list = Chat.objects.order_by("id_chat")
    chat_dict = {'chat': chat_list}

    return render(request, 'chat/Chat.html', context=chat_dict)