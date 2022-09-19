from turtle import home
from django.contrib import admin
from django.urls import path,include
from DataMundial.views import *

urlpatterns = [
    path('', inicio),
    path('DataMundial/', inicio),
    path('inicio/', inicio),
    path('registro/', registro),
    path('selecciones/', selecciones),
    path('concurso/', concurso),
    path('pronostico/', pronostico),
]