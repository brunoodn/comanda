from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import CadastroItem


def cadastrar_item(request):
    if request.method == 'POST':
        form = CadastroItem(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home/?status=1')
    else:
        return redirect('/home/?status=2')
