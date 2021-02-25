from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
  path('',views.chat),
  path('chat/',views.lista_publicacion),
  path('chat/<slug:value>/',views.detalles_publicacion),
]