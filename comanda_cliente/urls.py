from django.urls import path
from . import views

urlpatterns = [
    path('cadastrar_comanda/', views.cadastrar_comanda, name='cadastrar_comanda'),

]