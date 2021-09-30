from django import template

register = template.Library()

@register.filter
def total_linha(valor, qtd):
    return valor * qtd

@register.simple_tag
def total_comanda(valor, qtd):
    total = valor*qtd

    return total