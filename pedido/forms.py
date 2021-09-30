from django import forms
from .models import Pedido


class CadastroPedido(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = { 'id_comanda','id_item', 'quantidade' }
