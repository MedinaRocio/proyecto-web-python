from django.shortcuts import render, redirect

from .forms import formulario_de_contacto

from django.core.mail import EmailMessage

# Create your views here.
def contacto(request):
    
    formulario_contacto=formulario_de_contacto()
    
    if request.method=="POST":
        formulario_contacto=formulario_de_contacto(data=request.POST)
        if formulario_contacto.is_valid():
            nombre=request.POST.get("nombre")
            email=request.POST.get("email")
            contenido=request.POST.get("contenido")
            
            
            email=EmailMessage("Mensaje desde App Django", "El usuario con nombre {} con la direccion {} esrcribe: \n\n {}".format(nombre, email, contenido),"",["medinagonirocio@gmail.com"], reply_to=[email])
            
            try:
                email.send()
            
                return redirect("/contacto/?valido")
            
            except:
                
                return redirect("/contacto/?novalido")
                
    return render(request, 'contacto/contacto.html', {'mi_formulario':formulario_contacto}) 
                            