from django.shortcuts import render, redirect

from .carrito import Carrito

from tiendaApp.models import producto


# Create your views here.
def agregar(request, producto_id):
    carrito=Carrito(request)
    Producto=producto.objects.get(id=producto_id)
    carrito.agregar_producto(producto=Producto)
    
    return redirect("tienda")

def eliminar(request, producto_id):
    carrito=Carrito(request)
    Producto=producto.objects.get(id=producto_id)
    carrito.eliminar_producto(producto=Producto)
    
    return redirect("tienda")


def restar(request, producto_id):
    carrito=Carrito(request)
    Producto=producto.objects.get(id=producto_id)
    carrito.restar_unidades(producto=Producto)
    
    return redirect("tienda")

def limpiar(request, producto_id):
    carrito=Carrito(request)
    carrito.limpiar_carrito()
    
    return redirect("tienda")