from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from chats.models import Chat
from usuario.models import Usuario
from rest_framework.parsers import JSONParser
from chats.serializer import ChatSerializer

# Create your views here.
def chat(request):
    
    chat_list = Chat.objects.order_by("id_chat")
    chat_dict = {'chat': chat_list}

    return render(request,'chats/Chat.html', context=chat_dict)

@csrf_exempt
def lista_chat(request):
    if request.method == "GET":
        try:
            chat = Chat.objects.all()
            serializer = ChatSerializer(chat,many=True)
            return JsonResponse(serializer.data,safe=False,status=200)
        except:
            if serializer.errors:
                return HttpResponse(status=404)
            else:
                return HttpResponse(status=500)
    elif request.method == "POST":
        try:
            data = JSONParser().parse(request)
            serializer = ChatSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=201)
        except:
            if serializer.errors:
                return HttpResponse(serializer.errors, status=404)

@csrf_exempt
def detalles_chat(request,value):
    try:
        chat = Chat.objects.get(id_chat=value)
    except Chat.DoesNotExist:
        return HttpResponse(status=404)


    if request.method == "GET":
        try:
            serializer = ChatSerializer(chat)
            return JsonResponse(serializer.data,safe=False,status=200)
        except:
            if serializer.errors:
                return HttpResponse(status=404)
            else:
                return HttpResponse(status=500)

    
    elif request.method == "PUT":
        try:
            data = JSONParser().parse(request)
            serializer = ChatSerializer(chat,data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=200)
        except:
            if serializer.errors:
                return HttpResponse(status=404)
            else:
                HttpResponse(status=500)


    elif request.method == "DELETE":
        try:
            chat.delete()
            return HttpResponse(status=200)
        
        except:
            if chat.DoesNotExist():
                return HttpResponse(status=409)
            else:
                return HttpResponse(status=500)
    
