from django.contrib import admin
from django.urls import path
from publicacion import views
urlpatterns = [
  path('publicacion/',views.lista_publicacion),
  path('historia/',views.lista_historia),
  path('publicacion/<slug:value>/',views.detalles_publicacion),
  path('historias/<slug:value>/',views.detalles_historia)
]
