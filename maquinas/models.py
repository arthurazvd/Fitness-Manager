from django.db import models
from funcionarios.models import Funcionarios

class Maquinas(models.Model):
    id = models.AutoField(primary_key=True)
    maquina = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    idfun = models.ForeignKey(Funcionarios, on_delete=models.CASCADE)

    def __str__(self):
        return self.maquina
