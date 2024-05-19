from django.shortcuts import render
from carrito.carrito import Carrito

# Create your views here.

def Inicio(request):
    carro = Carrito(request)
    return render(request, 'app/inicio.html')


