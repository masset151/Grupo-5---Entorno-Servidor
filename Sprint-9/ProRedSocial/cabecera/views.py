from cabecera.models import Cabecera
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from chats.models import Chat
from usuario.models import Usuario
from rest_framework.parsers import JSONParser
from cabecera.serializer import CabeceraSerializer

# Create your views here.
def cabecera(request):
    cab_list = Cabecera.objects.order_by("usuario.nombre")
    cab_dict = {'cabecera': cab_list}
    
    return render(request,'cabecera/Cabecera.html', context=cab_dict)
@csrf_exempt
def lista_cabecera(request):
    if request.method == "GET":
        try:
            cabecera = Cabecera.objects.all()
            serializer = CabeceraSerializer(cabecera,many=True)
            return JsonResponse(serializer.data,safe=False,status=200)
        except:
            if cabecera.objects.DoesNotExist:
                return HttpResponse(status=404)
    elif request.method == "POST":
        try:
            data = JSONParser().parse(request)
            serializer = CabeceraSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=201)
        except:
            if serializer.errors:
                return HttpResponse(status=404)
            else:
                return HttpResponse(status=500)

@csrf_exempt
def detalles_cabecera(request,value):
    try:
        cabecera = Cabecera.objects.get(usuario=value)
    except Cabecera.DoesNotExist:
        return HttpResponse(status=404)


    if request.method == "GET":
        try:
            serializer = CabeceraSerializer(cabecera)
            return JsonResponse(serializer.data,safe=False,status=200)
        except: 
            if serializer.errors:
                return HttpResponse(status=404)
            else:
                return HttpResponse(status=500)


    
    elif request.method == "PUT":
        try:
            data = JSONParser().parse(request)
            serializer = CabeceraSerializer(cabecera,data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=200)
        except:
            if serializer.errors:
                return JsonResponse(status=204)

    elif request.method == "DELETE":
        try:
            cabecera.delete()
            return HttpResponse(status=200)
        
        except:
            if cabecera.DoesNotExist():
                return HttpResponse(status=409)
            else: 
                return HttpResponse(status=500)
    
