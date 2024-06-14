from django import forms
from .models import Usuario, Juego, Pedido

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
    
class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['usuario', 'juego']
        exclude = ['fecha_pedido']

