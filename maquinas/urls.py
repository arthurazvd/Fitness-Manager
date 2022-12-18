from django.contrib import admin
from django.urls import path, include
from .views import maquinas, nova_maquina, editar_maquina, apagar_maquina

urlpatterns = [
    path('', maquinas, name='maquinas'),
    path('nova-maquina/', nova_maquina, name='nova-maquina'),
    path('editar-maquina/<int:id>/', editar_maquina, name='editar-maquina'),
    path('apagar-maquina/<int:id>/', apagar_maquina, name='apagar-maquina'),
]