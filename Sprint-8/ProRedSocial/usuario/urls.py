from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
  path('',views.usuario),
  path('usuarios/',views.lista_usuario),
  path('usuarios/<slug:value>/',views.detalles_usuario),
]