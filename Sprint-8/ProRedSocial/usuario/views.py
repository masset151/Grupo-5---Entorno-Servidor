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
        usuario = Usuario.objects.all()
        serializer = UsuarioSerializer(usuario,many=True)
        return JsonResponse(serializer.data,safe=False,status=200)
    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = UsuarioSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)

        return JsonResponse(serializer.errors, status=204)

@csrf_exempt
def detalles_usuario(request,value):
    try:
        usuario = Usuario.objects.get(id_usuario=value)
    except Usuario.DoesNotExist:
        return HttpResponse(status=404)


    if request.method == "GET":
        serializer = UsuarioSerializer(usuario)
        return JsonResponse(serializer.data,safe=False,status=200)

    
    elif request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = UsuarioSerializer(usuario,data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)

        return JsonResponse(serializer.errors, status=204)

    elif request.method == "DELETE":
        try:
            usuario.delete()
            return HttpResponse(status=200)
        
        except:
    
            return HttpResponse(status=409)
    