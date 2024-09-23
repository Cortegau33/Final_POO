from django.shortcuts import render, redirect
from .models import Producto, Categoria, Proveedor, Cliente, Venta
from . forms import VentaForm,Venta, CategoriaForm, ProveedorForm, ClienteForm

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'ventas/lista_productos.html', {'productos': productos})

def registrar_venta(request):
    if request.method == 'POST':
        form = VentaForm(request.POST)
        if form.is_valid():
            venta = form.save(commit=False)
            venta.total = venta.producto.precio * venta.cantidad
            venta.save()
            return redirect('lista_ventas')  
    else:
        form = VentaForm()
    
    return render(request, 'ventas/registrar_venta.html', {'form': form})

def lista_ventas(request):
    ventas = Venta.objects.all()
    return render(request, 'ventas/lista_ventas.html', {'ventas': ventas})

def lista_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'ventas/lista_categorias.html', {'categorias': categorias})

def registrar_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_categorias')  # Asegúrate de que 'lista_categorias' esté definido en tus URL
    else:
        form = CategoriaForm()

    return render(request, 'ventas/registrar_categoria.html', {'form': form})

def lista_proveedores(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'ventas/lista_proveedores.html', {'proveedores': proveedores})

def registrar_proveedor(request):
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_proveedores')  # Asegúrate de que 'lista_proveedores' esté definido en tus URL
    else:
        form = ProveedorForm()

    return render(request, 'ventas/registrar_proveedor.html', {'form': form})

def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'ventas/lista_clientes.html', {'clientes': clientes})

def registrar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')  # Asegúrate de que 'lista_clientes' esté definido en tus URL
    else:
        form = ClienteForm()

    return render(request, 'ventas/registrar_cliente.html', {'form': form})