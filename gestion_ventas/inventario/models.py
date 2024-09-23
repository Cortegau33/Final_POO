from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return str(self.nombre)

class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    contacto = models.CharField(max_length=100)
    direccion = models.TextField()

    def __str__(self):
        return str(self.nombre)

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.SET_NULL, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()

    def __str__(self):
        return str(self.nombre)

class Cliente(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)  
    telefono = models.CharField(max_length=15)
    direccion = models.TextField()

    def __str__(self):
        return str(self.usuario.username)

class Venta(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    total = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_venta = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Venta {self.id} - {self.producto.nombre} a {self.cliente.usuario.username}'
