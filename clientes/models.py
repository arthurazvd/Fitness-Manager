from django.db import models
from funcionarios.models import Funcionarios

class Clientes(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    idade = models.IntegerField()
    email = models.EmailField()
    telefone = models.IntegerField()

    def __str__(self):
        return self.nome

class ConsulClientes(models.Model):
    id = models.AutoField(primary_key=True)
    idcli = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    idfun = models.ForeignKey(Funcionarios, on_delete=models.CASCADE)


