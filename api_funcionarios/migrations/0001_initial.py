# Generated by Django 5.0.2 on 2024-02-16 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('funcionario_id', models.CharField(default='', max_length=10, primary_key=True, serialize=False, unique=True)),
                ('funcionario_nome', models.CharField(default='', max_length=150)),
                ('funcionario_data_nascimento', models.DateField(default='', max_length=10)),
                ('funcionario_endereco', models.CharField(default='', max_length=150)),
                ('funcionario_cpf', models.CharField(default='', max_length=12)),
                ('funcionario_ec', models.CharField(default='', max_length=50)),
            ],
        ),
    ]
