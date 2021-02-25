from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
  path('',views.cabecera),
  path('cabecera/',views.lista_cabecera),
  path('cabecera/<slug:value>/',views.detalles_cabecera),
]