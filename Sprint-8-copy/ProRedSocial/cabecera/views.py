from django.shortcuts import render
from django.http import HttpResponse
from usuario.models import Usuario
from cabecera.models import Cabecera

# Create your views here.
def cabecera(request):
    cab_list = Cabecera.objects.order_by("usuario.nombre")
    cab_dict = {'cabecera': cab_list}
    
    return render(request,'cabecera/Cabecera.html', context=cab_dict)