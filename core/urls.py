from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home),
    path('home/', views.home, name='home'),
    path('item/', include('item.urls'), name='item'),
    path('comanda/,',include('comanda_cliente.urls'), name='comanda_cliente' ),
    path('pedido/', include('pedido.urls'), name='pedido'),
]