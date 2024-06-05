from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('crear_juego/', views.crear_juego, name='crear_juego'),
    path('buscar_juego/', views.buscar_juego, name='buscar_juego'),
    path('crear_pedido/', views.crear_pedido, name='crear_pedido'),
    path('registro_usuario/', views.registro_usuario, name='registro_usuario'),
]
