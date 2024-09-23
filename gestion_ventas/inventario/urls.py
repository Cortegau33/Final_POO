from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('productos/', views.lista_productos, name='lista_productos'),
    path('registrar-venta/', views.registrar_venta, name='registrar_venta'),
    path('ventas/', views.lista_ventas, name='lista_ventas'),
    path('categorias/', views.lista_categorias, name='lista_categorias'),
    path('registrar-categoria/', views.registrar_categoria, name='registrar_categoria'),
    path('proveedores/', views.lista_proveedores, name='lista_proveedores'),
    path('registrar-proveedor/', views.registrar_proveedor, name='registrar_proveedor'),
    path('clientes/', views.lista_clientes, name='lista_clientes'),
    path('registrar-cliente/', views.registrar_cliente, name='registrar_cliente'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
