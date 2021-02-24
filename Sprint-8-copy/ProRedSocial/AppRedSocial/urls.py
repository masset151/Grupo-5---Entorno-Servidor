from django.contrib import admin
from django.urls import path,include
from AppRedSocial import views

urlpatterns = [
    path('',views.index)
    
]
