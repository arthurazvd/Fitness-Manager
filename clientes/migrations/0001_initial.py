# Generated by Django 4.1.1 on 2022-09-08 19:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('funcionarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=100)),
                ('cpf', models.CharField(max_length=11)),
                ('idade', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('telefone', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ConsulClientes',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('idcli', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientes.clientes')),
                ('idfun', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='funcionarios.funcionarios')),
            ],
        ),
    ]
