from django.shortcuts import render, redirect
from .forms import CadastroPedido
from .models import Pedido
from item.models import Item
# Create your views here.

def cadastrar_pedido(request):
    if request.method == 'POST':
        form = CadastroPedido(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home/?status_pedido=1')
    else:
        return redirect('/home/?status_pedido=2')

def ver_pedido(request, id):

    #pedido = Pedido.objects.filter(id_comanda=id) essa forma funciona com menos performance
    pedido = Pedido.objects.filter(id_comanda = id).select_related('id_item')

    content = {
        'pedido': pedido,

    }
    return render(request,'ver_pedido.html', content)
