from django.shortcuts import render
from .models import Usuario, Juego, Pedido
from .forms import UsuarioForm, JuegoForm, PedidoForm

def index(request):
    # Vista principal de la tienda
    return render(request, 'index.html')

def registro_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            # Aquí puedes redirigir a una página de éxito o cualquier otra acción
    else:
        form = UsuarioForm()
    return render(request, 'registro_usuario.html', {'form': form})

def crear_juego(request):
    if request.method == 'POST':
        form = JuegoForm(request.POST)
        if form.is_valid():
            form.save()
            # Aquí puedes redirigir a una página de éxito o cualquier otra acción
    else:
        form = JuegoForm()
    return render(request, 'crear_juego.html', {'form': form})

def crear_pedido(request):
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            form.save()
            # Aquí puedes redirigir a una página de éxito o cualquier otra acción
    else:
        form = PedidoForm()
    return render(request, 'crear_pedido.html', {'form': form})

def buscar_juego(request):
    juegos = None

    if request.method == 'GET':
        nombre = request.GET.get('nombre')
        id_juego = request.GET.get('id')
        rango_edades = request.GET.get('rango_edades')

        # Lógica para buscar juegos
        juegos = Juego.objects.all()

        if nombre:
            juegos = juegos.filter(nombre__icontains=nombre)

        if id_juego:
            juegos = juegos.filter(id=id_juego)

        if rango_edades:
            # Asumiendo que el rango de edades se almacena en formato "min-max"
            min_edad, max_edad = map(int, rango_edades.split('-'))
            juegos = juegos.filter(edad_recomendada__gte=min_edad, edad_recomendada__lte=max_edad)

    return render(request, 'buscar_juego.html', {'juegos': juegos})