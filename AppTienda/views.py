from django.shortcuts import render, redirect
from .forms import UsuarioForm, JuegoForm, BuscarJuegoForm
from .models import Juego
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm

def index(request):
    return render(request, 'index.html')

@login_required
def crear_juego(request):
    if request.method == 'POST':
        form = JuegoForm(request.POST, request.FILES)
        if form.is_valid():
            juego = form.save(commit=False)  
            juego.imagen = form.cleaned_data['imagen']  
            juego.save()  
            return redirect('index')
    else:
        form = JuegoForm()  
    return render(request, 'crear_juego.html', {'form': form})

def buscar_juego(request):
    juegos = []
    nombre = request.GET.get('nombre')
    edad_recomendada = request.GET.get('edad_recomendada')
    materiales = request.GET.get('materiales')

    if nombre or edad_recomendada or materiales:
        juegos = Juego.objects.all()
        if nombre:
            juegos = juegos.filter(nombre__icontains=nombre)
        if edad_recomendada:
            juegos = juegos.filter(edad_recomendada=edad_recomendada)
        if materiales:
            juegos = juegos.filter(materiales__icontains=materiales)

    return render(request, 'buscar_juego.html', {'juegos': juegos})

def about_me(request):
    return render(request, 'about_me.html')

def registro_usuario(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Usuario {username} creado correctamente.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registro_usuario.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('about_me')
    else:
        form = AuthenticationForm()
    
    return render(request, 'login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('index') 