from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
  path('publicacion',views.publicacion),
  path('historia',views.historia),
]
