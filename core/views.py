from re import template
from django.shortcuts import render
from .models import Producto

# Create your views here.

def productos(request):
    productos= Producto.objects.all()
    data = {
        'productos': productos
    }
    return render(request, 'core/productos.html', data)

def home(request):
    return render(request, 'core/Home.html')

def iniciar_sesion(request):
    return render(request, 'core/Iniciar_sesión.html')

