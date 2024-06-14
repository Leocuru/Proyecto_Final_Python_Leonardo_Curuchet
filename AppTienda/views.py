from django.shortcuts import render, redirect
from .forms import UsuarioForm, JuegoForm, PedidoForm
from .models import Juego

def index(request):
    return render(request, 'index.html')

def crear_juego(request):
    if request.method == 'POST':
        form = JuegoForm(request.POST, request.FILES)  # Incluir request.FILES para manejar archivos
        if form.is_valid():
            juego = form.save(commit=False)  # Guardar el formulario pero sin commit para manejar la imagen
            juego.imagen = form.cleaned_data['imagen']  # Asignar la imagen
            juego.save()  # Guardar el objeto Juego con la imagen asignada
            return redirect('index')  # Redireccionar a la página principal u otra página de confirmación
    else:
        form = JuegoForm()  # Formulario vacío para mostrar al principio
    return render(request, 'crear_juego.html', {'form': form})

def crear_pedido(request):
    juegos_disponibles = Juego.objects.all()
    
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            pedido = form.save(commit=False)
            juego_id = request.POST.get('juego')
            juego = Juego.objects.get(id=juego_id)
            pedido.juego = juego
            pedido.save()
            
            return redirect('index')
    else:
        form = PedidoForm()
    
    return render(request, 'crear_pedido.html', {'form': form, 'juegos_disponibles': juegos_disponibles})

def registro_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = UsuarioForm()
    return render(request, 'registro_usuario.html', {'form': form})

def buscar_juego(request):
    nombre = request.GET.get('nombre')
    id = request.GET.get('id')
    rango_edades = request.GET.get('rango_edades')

    juegos = Juego.objects.all()

    if nombre:
        juegos = juegos.filter(nombre__icontains=nombre)
    if id:
        juegos = juegos.filter(id=id)
    if rango_edades:
        edades = rango_edades.split('-')
        if len(edades) == 2:
            try:
                edad_min = int(edades[0])
                edad_max = int(edades[1])
                juegos = juegos.filter(edad_recomendada__gte=edad_min, edad_recomendada__lte=edad_max)
            except ValueError:
                pass

    return render(request, 'buscar_juego.html', {'juegos': juegos})