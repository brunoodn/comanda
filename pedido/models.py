from django.db import models
from comanda_cliente.models import ComandaCliente
from item.models import Item
# Create your models here.

class Pedido(models.Model):
    id_comanda = models.ForeignKey(ComandaCliente(), on_delete=models.DO_NOTHING)
    id_item = models.ForeignKey(Item, on_delete=models.DO_NOTHING)
    quantidade = models.IntegerField()
    ativo = models.BooleanField(default=True)
    data_criacao = models.DateField(auto_now_add=True)


