from django.contrib import admin
from django.urls import path, include
from .views import clientes, novo_cliente, editar_cliente, apagar_cliente

urlpatterns = [
    path('', clientes, name='clientes'),
    path('novo-cliente/', novo_cliente, name='novo-cliente'),
    path('editar-cliente/<int:id>/', editar_cliente, name='editar-cliente'),
    path('apagar-cliente/<int:id>/', apagar_cliente, name='apagar-cliente'),
]