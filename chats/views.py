from django.shortcuts import render
from django.http import HttpResponse
from chats.models import Chat
from usuario.models import Usuario

# Create your views here.
def chat(request):
    
    chat_list = Chat.objects.order_by("id_chat")
    chat_dict = {'chat': chat_list}

    return render(request,'chats/Chat.html', context=chat_dict)