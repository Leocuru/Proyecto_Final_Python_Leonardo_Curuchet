from django.test import TestCase
from django.urls import reverse
from .models import Juego

class JuegoModelTestCase(TestCase):
    def setUp(self):
        Juego.objects.create(nombre="Escondite", edad_recomendada=6, materiales="Ninguno", descripcion="Juego clásico de esconderse")
        Juego.objects.create(nombre="Rayuela", edad_recomendada=8, materiales="Tiza y piedras", descripcion="Juego de equilibrio y habilidad")
        Juego.objects.create(nombre="Ta Te Ti", edad_recomendada=5, materiales="Papel y lápiz", descripcion="Juego de estrategia simple")

    def test_juego_nombre(self):
        juego_escondite = Juego.objects.get(nombre="Escondite")
        juego_rayuela = Juego.objects.get(nombre="Rayuela")
        juego_tateti = Juego.objects.get(nombre="Ta Te Ti")
        self.assertEqual(juego_escondite.nombre, "Escondite")
        self.assertEqual(juego_rayuela.nombre, "Rayuela")
        self.assertEqual(juego_tateti.nombre, "Ta Te Ti")

    def test_buscar_juego_view(self):
        response = self.client.get(reverse('buscar_juego'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Buscar Juego")


