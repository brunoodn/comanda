from django.db import models

# Create your models here.

class ComandaCliente(models.Model):

    numero_mesa = models.CharField(max_length=10, name='numero_mesa')
    nome_cliente = models.CharField(max_length=50, name='nome_cliente')
    ativo = models.BooleanField(default=True)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome_cliente


