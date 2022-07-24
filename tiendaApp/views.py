from django.shortcuts import render

from .models import producto

# Create your views here.

def tienda(request):
    
    mostrar_productos=producto.objects.all()
    
    return render(request, 'tienda/tienda.html', {"mostrar_productos":mostrar_productos})