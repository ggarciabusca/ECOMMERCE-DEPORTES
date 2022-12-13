from django.db import models
from django.contrib.auth.models import User
from productos.models import *

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares',null=True,blank=True,default="/default.jpeg")

#Creacion de la app para mensajes
class Mensajes(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE)
    mensaje = models.CharField(max_length=300)
    fecha = models.DateTimeField(auto_now=True)

    #Para mostrar los campos con el nombre en la pantalla de admin
    def __str__(self):
        return f"User FK : {self.user} - Arituclo FK: {self.articulo} - Mensaje: {self.mensaje} - Fecha: {self.fecha}"
