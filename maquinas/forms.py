from django import forms
from .models import Maquinas

class FormMaquina(forms.ModelForm):
    class Meta:
        model = Maquinas
        fields = ['id', 'maquina', 'estado', 'idfun']


