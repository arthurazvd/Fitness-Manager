from django.shortcuts import render, redirect
from .models import Funcionarios
from .forms import FormFuncionario

def funcionarios(request):
    funcionarios = Funcionarios.objects.all()
    return render(request, 'funcionarios.html', {'funcionarios':funcionarios} )

def novo_funcionario(request):
    form = FormFuncionario(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('funcionarios')

    return render(request, 'funcionarios-novo.html', {'form': form})

def editar_funcionario(request, id):
    funcionarios = Funcionarios.objects.get(id=id)
    form = FormFuncionario(request.POST or None, instance=funcionarios)

    if form.is_valid():
        form.save()
        return redirect('funcionarios')

    return render(request, 'funcionarios-editar.html', {'form': form, 'funcionarios':funcionarios})

def apagar_funcionario(request, id):
    funcionarios = Funcionarios.objects.get(id=id)

    funcionarios.delete()
    return redirect('funcionarios')

