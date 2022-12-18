from django import forms
from .models import Funcionarios

class FormFuncionario(forms.ModelForm):
    class Meta:
        model = Funcionarios
        fields = ['id', 'nome', 'cpf', 'email', 'telefone', 'idade', 'tipo']