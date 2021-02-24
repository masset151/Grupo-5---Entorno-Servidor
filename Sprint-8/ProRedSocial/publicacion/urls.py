from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
  path('',views.publicacion),
  path('',views.historia),
  path('publicacion/',views.lista_publicacion),
  path('historia/',views.lista_historia),
  path('publicacion/<slug:value>',views.detalles_publicacion),
  path('historias/<slug:value>',views.detalles_historia)
]
