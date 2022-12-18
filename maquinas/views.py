from django.shortcuts import render, redirect
from .models import Maquinas
from .forms import FormMaquina

def maquinas(request):
    maquinas = Maquinas.objects.all()
    return render(request, 'maquinas.html', {'maquinas':maquinas} )

def nova_maquina(request):
    maq = FormMaquina(request.POST or None)

    if maq.is_valid():
        maq.save()
        return redirect('maquinas')

    return render(request, 'maquinas-novo.html', {'maq': maq})

def editar_maquina(request, id):
    maquinas = Maquinas.objects.get(id=id)
    maq = FormMaquina(request.POST or None, instance=maquinas)
   
   
    if maq.is_valid():
        maq.save()
        return redirect('maquinas')

    return render(request, 'maquinas-editar.html', {'maq': maq, 'maquinas':maquinas})

def apagar_maquina(request, id):
    maquinas = Maquinas.objects.get(id=id)

    maquinas.delete()
    return redirect('maquinas')

