from django.shortcuts import render
from django.http import HttpResponse
from item.models import Item
from comanda_cliente.models import ComandaCliente
from item.forms import CadastroItem
from comanda_cliente.forms import CadastroComanda
from pedido.forms import CadastroPedido
# Create your views here.

def home(request):
    comanda = ComandaCliente.objects.filter(ativo=True)
    form_item = CadastroItem()
    form_comanda = CadastroComanda()
    form_pedido = CadastroPedido()
    content = {'form_item': form_item, 'form_comanda': form_comanda, 'form_pedido': form_pedido, 'comanda': comanda }
    return render(request, 'home.html', content)

