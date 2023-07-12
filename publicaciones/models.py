from django.db import models

# Create your models here.

'''    Categoría:
nombre: texto de 200 caracteres, único.
activo: booleano, por defecto True.
creacion: fecha y hora automática de creación.
actualizacion: fecha y hora automática de actualización.
El modelo Categoria debe ordenarse por el campo nombre.
Sobre escribir el método __str__ para que retorne el campo nombre.'''

class Categoría(models.Model):
    nombre = models.CharField(max_length = 200)
    activo = models.BooleanField(default = True)
    creado = models.DateField(auto_now_add = True)
    actualizado = models.DateField(auto_now_add = True)
    def __str__(self):
        return self.nombre
    






