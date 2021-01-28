from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("registro/",include('registro.urls')),
    path("publicacion/",include('publicacion.urls')),
    path('help/',admin.site.urls)
   
]
