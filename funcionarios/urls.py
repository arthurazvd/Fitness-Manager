from django.contrib import admin
from django.urls import path, include
from .views import funcionarios, novo_funcionario, editar_funcionario, apagar_funcionario

urlpatterns = [
    path('', funcionarios, name='funcionarios'),
    path('novo-funcionario/', novo_funcionario, name='novo-funcionario'),
    path('editar-funcionario/<int:id>/', editar_funcionario, name='editar-funcionario'),
    path('apagar-funcionario/<int:id>/', apagar_funcionario, name='apagar-funcionario'),
]