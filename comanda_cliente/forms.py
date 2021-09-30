from django.forms import ModelForm
from .models import ComandaCliente

class CadastroComanda(ModelForm):
    class Meta:
        model = ComandaCliente
        fields = {'nome_cliente','numero_mesa' }
