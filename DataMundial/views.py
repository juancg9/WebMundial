from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'home.html')

def inicio(request):
    return render(request, 'inicio.html')

def inicio2(request):
    return render(request, 'inicio2.html')

def registro(request):
    return render(request, 'registro.html')

def selecciones(request):
    return render(request, 'selecciones.html')

def concurso(request):
    return render(request, 'concurso.html')

def pronostico(request):
    return render(request, 'pronostico.html')
