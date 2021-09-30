from django.db import models

# Create your models here.

class Item(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(decimal_places=2, max_digits=8)

    def __str__(self):
        return self.nome