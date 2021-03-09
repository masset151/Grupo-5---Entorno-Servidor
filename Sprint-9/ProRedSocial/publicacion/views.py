from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from publicacion.models import Publicacion, ConsultarPublicacion, Historia, VerHistoria
from usuario.models import Usuario
from rest_framework.parsers import JSONParser
from publicacion.serializer import PublicacionSerializer, HistoriaSerializer

# Create your views here.


def publicacion(request):
    pu_list = Publicacion.objects.order_by("id_publicacion")
    pu_dict = {'publicacion': pu_list}

    return render(request, 'publicacion/publicacion.html', context=pu_dict)


def historia(request):
    his_list = Historia.objects.order_by("id_historia")
    his_dict = {'historia': his_list}

    return render(request, 'publicacion/historia.html', context=his_dict)


def chat(request):

    chat_list = Chat.objects.order_by("id_chat")
    chat_dict = {'chat': chat_list}

    return render(request, 'chat/Chat.html', context=chat_dict)


@csrf_exempt
def lista_publicacion(request):
    if request.method == "GET":
        try:
            publicacion = Publicacion.objects.all()
            serializer = PublicacionSerializer(publicacion, many=True)
            return JsonResponse(serializer.data, safe=False, status=200)
        except:
            if Publicacion.DoesNotExist():
                return HttpResponse(status=400)
            else:
                return HttpResponse(status=500)
    elif request.method == "POST":
        try:
            data = JSONParser().parse(request)
            serializer = PublicacionSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=201)
        except:
            if serializer.errors:
                return HttpResponse(status=404)
            else:
                return HttpResponse(status=500)


@csrf_exempt
def detalles_publicacion(request, value):
    try:
        publicacion = Publicacion.objects.get(id_publicacion=value)
    except Publicacion.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == "GET":
        try:
            serializer = PublicacionSerializer(publicacion)
            return JsonResponse(serializer.data, safe=False, status=200)
        except:
            if serializer.errors:
                return HttpResponse(status=404)
            else:
                return HttpResponse(status=500)

    elif request.method == "PUT":
        try:
            data = JSONParser().parse(request)
            serializer = PublicacionSerializer(publicacion, data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=200)
            else:

                return JsonResponse(serializer.errors, status=204)
        except:
            if serializer.errors:
                return HttpResponse(status=400)
            else:
                return HttpResponse(status=500)

    elif request.method == "DELETE":
        try:
            publicacion.delete()
            return HttpResponse(status=200)

        except:
            if publicacion.DoesNotExist():
                return HttpResponse(status=409)
            else:
                return HttpResponse(status=500)


@csrf_exempt
def lista_historia(request):
    if request.method == "GET":
        try:  
            historia = Historia.objects.all()
            serializer = HistoriaSerializer(historia, many=True)
            return JsonResponse(serializer.data, safe=False, status=200)
        except:
            if serializer.errors:
                return HttpResponse(status=400)
            else:
                return HttpResponse(status=500)

    elif request.method == "POST":
        try:
            data = JSONParser().parse(request)
            serializer = HistoriaSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=201)
        except:
            if serializer.errors:
                return HttpResponse(status=404)
            else:
                return HttpResponse(status=500)


@csrf_exempt
def detalles_historia(request, value):
    try:
        historia = Historia.objects.get(id_historia=value)
    except Historia.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == "GET":
        try:
            serializer = HistoriaSerializer(historia)
            return JsonResponse(serializer.data, safe=False, status=200)
        except:
            if serializer.errors:
                return HttpResponse(status=404)
            else:
                return HttpResponse(status=505)

    elif request.method == "PUT":
        try:
            data = JSONParser().parse(request)
            serializer = HistoriaSerializer(historia, data=data)
        
            if serializer.is_valid():
                serializer.save()
            return JsonResponse(serializer.data, status=200)
        except:
            if serializer.errors:
                return HttpResponse(status=404)
            else:
                return HttpResponse(status=500)
                

    elif request.method == "DELETE":
        try:
            historia.delete()
            return HttpResponse(status=200)

        except:
            if historia.DoesNotExist():
                return HttpResponse(status=409)
            else:
                return HttpResponse(status=500)
