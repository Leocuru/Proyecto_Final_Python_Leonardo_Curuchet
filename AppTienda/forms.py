from django import forms
from .models import Usuario, Juego, Pedido

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'email', 'edad']

class JuegoForm(forms.ModelForm):
    class Meta:
        model = Juego
        fields = ['nombre', 'edad_recomendada', 'descripcion']

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['usuario', 'juego']
        exclude = ['fecha_pedido']

