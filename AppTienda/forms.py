from django import forms
from .models import Usuario, Juego

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'email', 'edad']

class JuegoForm(forms.ModelForm):
    imagen = forms.ImageField(label='Imagen', required=True)
    materiales = forms.CharField(label='Materiales necesarios', widget=forms.Textarea)

    
    class Meta:
        model = Juego
        fields = ['nombre', 'edad_recomendada', 'descripcion', 'imagen', 'materiales']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Ingrese el nombre del juego'})
        self.fields['edad_recomendada'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Ingrese la edad recomendada'})
        self.fields['descripcion'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Ingrese la descripción del juego'})
        self.fields['imagen'].widget.attrs.update({'class': 'form-control-file'})
        self.fields['materiales'].widget.attrs.update({'class': 'form-control', 'rows': 4, 'placeholder': 'Detalla los materiales necesarios'})
    
class BuscarJuegoForm(forms.Form):
    nombre = forms.CharField(max_length=100, required=False)
    edad_recomendada = forms.IntegerField(required=False)
    rango_edades = forms.CharField(max_length=7, required=False)
    materiales = forms.CharField(max_length=255, required=False)
