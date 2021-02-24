from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from AppRedSocial.models import User
from AppRedSocial.serializer import UserSerializer



# Create your views here.


def index(request):
    
    return render(request, 'index/index.html')


@csrf_exempt
def user_list(request):

    if request.method == "GET":
        users = User.objects.all()
        serializer = UserSerializer(users,many=True)
        return JsonResponse(serializer.data,safe=False,status=200)
    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)

        return JsonResponse(serializer.errors, status=204)

@csrf_exempt
def user_details(request,value):
    try:
        user = User.objects.get(nick=value)
    except User.DoesNotExist:
        return HttpResponse(status=404)


    if request.method == "GET":
        serializer = UserSerializer(user)
        return JsonResponse(serializer.data,safe=False,status=200)

        

    
    elif request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = UserSerializer(user,data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)

        return JsonResponse(serializer.errors, status=204)

    elif request.method == "DELETE":
        try:
            user.delete()
            return HttpResponse(status=200)
        
        except:
    
            return HttpResponse(status=409)
    