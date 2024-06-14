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
    materiales = models.TextField()  # Campo para los materiales necesarios

    def __str__(self):
        return self.nombre

class Pedido(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    juego = models.ForeignKey(Juego, on_delete=models.CASCADE, default=None)
    fecha_pedido = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'Pedido {self.id} - {self.usuario.nombre}'
