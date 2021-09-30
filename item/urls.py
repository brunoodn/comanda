from django.urls import path
from .views import cadastrar_item

urlpatterns = [
    path('cadastrar_item/', cadastrar_item, name='cadastrar_item' ),

]