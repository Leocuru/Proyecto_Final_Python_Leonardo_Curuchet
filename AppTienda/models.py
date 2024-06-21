from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    edad = models.IntegerField()
    
    def __str__(self):
        return self.nombre

class Juego(models.Model):
    nombre = models.CharField(max_length=100)
    edad_recomendada = models.IntegerField(default=0)
    descripcion = models.TextField()
    materiales = models.TextField(default='Sin especificar')
    imagen = models.ImageField(upload_to='juegos/', blank=True, null=True) 

    def __str__(self):
        return self.nombre

