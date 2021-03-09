from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from usuario.models import Usuario
from usuario.serializer import UsuarioSerializer

# Create your views here.


def usuario(request):
    users_list = Usuario.objects.order_by("id_usuario")
    usuarios_dict = {'usuarios': users_list}

    return render(request, 'usuario/Usuario.html', context=usuarios_dict)


@csrf_exempt
def lista_usuario(request):

    if request.method == "GET":
        try:
            usuario = Usuario.objects.all()
            serializer = UsuarioSerializer(usuario, many=True)
            return JsonResponse(serializer.data, safe=False, status=200)

        except:
            if Usuario.objects.DoesNotExist:
                return HtppResponse(status=404)
            else:
                return HtppResponse(status=500)

    elif request.method == "POST":
        try:
            data = JSONParser().parse(request)
            serializer = UsuarioSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=201)

            return JsonResponse(serializer.errors, status=204)
        except:
            if not serializer.is_valid():
                return HtppResponse(status=400)
            return HtppResponse(status=500)


@csrf_exempt
def detalles_usuario(request, value):
    try:
        usuario = Usuario.objects.get(id_usuario=value)
    except: 
        if  Usuario.DoesNotExist:
            return HttpResponse(status=404)
        else :
            return HttpResponse(status=504)

    if request.method == "GET":

        try:
            serializer = UsuarioSerializer(usuario)
            return JsonResponse(serializer.data, safe=False, status=200)
        except:
            return HtppResponse(Exception, status=400)

    elif request.method == "PUT":
        try:
            data = JSONParser().parse(request)
            serializer = UsuarioSerializer(usuario, data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=200)

            return JsonResponse(serializer.errors, status=204)

        except:
            if not serializer.is_valid:
                return HtppResponse(status=400)
            else: 
                return HtppResponse(status=500)

    elif request.method == "DELETE":
        try:
            usuario.delete()
            return HttpResponse(status=200)

        except:
            if usuario.DoesNotExist():
                return HttpResponse(status=409)
            else:
                return HttpResponse(status=500)