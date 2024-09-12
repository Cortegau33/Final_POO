import csv
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.dateparse import parse_date
from django.http import HttpResponse
from .models import Categoria, Proveedor, Producto, Cliente, Venta