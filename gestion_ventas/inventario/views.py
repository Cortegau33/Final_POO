from django.shortcuts import render, get_object_or_404
from .models import Producto

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'ventas/lista_productos.html', {'productos': productos})