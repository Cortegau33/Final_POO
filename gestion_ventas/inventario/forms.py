from django import forms
from .models import Categoria, Proveedor, Producto, Cliente, Venta

class CategoriaForm(forms.ModelForm):
    class Meta:
        Model: Categoria
        fields = ['nombre', 'descripcion']

class ProveedorForm(forms.Modelform):
    class Meta:
        Model: Proveedor
        Fields = ['nombre', 'contacto', 'telefono']

class ProductoForm(forms.Modelform):
    class Meta:
        Model: Producto
        fields = ['nombre', 'categoria', 'proveedor', 'etiquetas', 'cantidad', 'precio', 'descripcion']
        widgets = {
            'etiquetas': forms.CheckboxSelectMultiple(),
        }

class ClienteForm(forms.Modelform):
    class Meta:
        Model: Cliente
        fields = ['nombre', 'telefono', 'email', 'direccion']
        

