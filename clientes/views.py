from django.shortcuts import render, redirect
from .models import Clientes
from .forms import FormCliente

def clientes(request):
    clientes = Clientes.objects.all()
    return render(request, 'clientes.html', {'clientes':clientes} )

def novo_cliente(request):
    form = FormCliente(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('clientes')

    return render(request, 'clientes-novo.html', {'form': form})

def editar_cliente(request, id):
    clientes = Clientes.objects.get(id=id)
    form = FormCliente(request.POST or None, instance=clientes)

    if form.is_valid():
        form.save()
        return redirect('clientes')

    return render(request, 'clientes-editar.html', {'form': form, 'clientes':clientes})

def apagar_cliente(request, id):
    clientes = Clientes.objects.get(id=id)

    clientes.delete()
    return redirect('clientes')

