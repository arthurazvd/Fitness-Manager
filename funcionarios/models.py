from django.db import models

class Funcionarios(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    senha = models.CharField(max_length=8)
    email = models.EmailField()
    telefone = models.IntegerField()
    tipo = models.IntegerField()
    idade = models.IntegerField()

    def __str__(self):
        return self.nome
    
