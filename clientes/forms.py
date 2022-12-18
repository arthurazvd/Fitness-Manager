from django import forms
from .models import Clientes

class FormCliente(forms.ModelForm):
    class Meta:
        model = Clientes
        fields = ['id', 'nome', 'cpf', 'email', 'telefone', 'idade']