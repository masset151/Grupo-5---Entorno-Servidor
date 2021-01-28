from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def usuario(request):
    context = {
        'user_var':{'1':"PEPE2222"},
        'url_img':{'URL'}

        #AñadirCamposdelFormulario
    }
    return render(request,'usuario//Usuario.html', context)