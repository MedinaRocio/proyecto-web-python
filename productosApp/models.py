from email.headerregistry import ContentDispositionHeader
from ssl import create_default_context
from tkinter import image_names
from django.db import models

# Create your models here.

class producto (models.Model):
    titulo=models.CharField(max_length=50)
    contenido=models.CharField(max_length=50)
    imagen=models.ImageField(upload_to='productos')
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)
    
    class meta:
        verbose_name='producto'
        verbose_name_plural='productos'
        
    def __str__(self):
        return self.titulo