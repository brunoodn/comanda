from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CadastroComanda

def cadastrar_comanda(request):
    if request.method == 'POST':
        form = CadastroComanda(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home/?status_comanda=1')
    else:
        return redirect('/home/?status_comanda=2')
