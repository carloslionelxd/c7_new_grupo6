from django.db import models
from django.contrib.auth.models import User

# Create your models here.

'''    Categoría:
nombre: texto de 200 caracteres, único.
activo: booleano, por defecto True.
creacion: fecha y hora automática de creación.
actualizacion: fecha y hora automática de actualización.
El modelo Categoria debe ordenarse por el campo nombre.
Sobre escribir el método __str__ para que retorne el campo nombre.
'''

class Categoría(models.Model):
    nombre = models.CharField(max_length=200, unique=True)
    activo = models.BooleanField(default=True)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

    class Meta:
        ordering = ['nombre']

    
"""
Etiqueta
nombre: texto de 200 caracteres, único.
activo: booleano, default TRUE.
creacion: fecha y hora automática de creación.
actualizacion: fecha y hora automática de actualización.
El modelo Etiqueta debe ordenarse por el campo nombre.
Sobre escribir el método __str__ para que retorne el campo nombre.
"""

class Etiqueta(models.Model):
    nombre = models.CharField(max_length = 200)
    activo = models.BooleanField(default = True)
    creacion = models.DateTimeField(auto_now_add = True)
    actualizacion = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.nombre
    
    class Meta:
        ordering = ['nombre'] 

"""
Articulo:
titulo: texto 250 caracteres.
bajada: texto 600 caracteres.
contenido: texto.
imagen: campo imagen, debe permitir valores nulos, guardar en carpeta articulo.
publicado: booleano, por defecto False.
categoria: relación uno a muchos con modelo Categoria. Borrado SET_NULL.
autor: relación uno a muchos con modelo User. Borrado SET_NULL.
etiqueta: relación muchos a muchos con modelo Etiqueta.
creacion: fecha y hora automática de creación.
actualizacion: fecha y hora automática de actualización.
El modelo Articulo debe ordenarse por el campo creacion.
Sobre escribir el método __str__ para que retorne el campo titulo
"""

class Articulo(models.Model):
    titulo = models.CharField(max_length = 250)
    bajada = models.CharField(max_length = 600)
    contenido = models.TextField()
    imagen = models.ImageField(upload_to='articulo/', null=True, blank=True)
    publicado = models.BooleanField(default=False)
    categoria = models.ForeignKey(Categoría, on_delete=models.SET_NULL, null=True)
    autor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    etiqueta = models.ManyToManyField(Etiqueta)
    creacion = models.DateTimeField(auto_now_add=True)
    actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo

    class Meta:
        ordering = ['-creacion']