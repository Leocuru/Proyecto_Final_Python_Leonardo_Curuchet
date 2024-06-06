from django.urls import path
from .views import index, crear_juego, crear_pedido, buscar_juego, registro_usuario

urlpatterns = [
    path('', index, name='index'),
    path('crear_juego/', crear_juego, name='crear_juego'),
    path('buscar_juego/', buscar_juego, name='buscar_juego'),
    path('crear_pedido/', crear_pedido, name='crear_pedido'),
    path('registro_usuario/', registro_usuario, name='registro_usuario'),
]
