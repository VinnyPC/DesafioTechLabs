from django.db import models


# Nome Completo
# Data de nascimento
# Endereço
# CPF
# Estado Civil

class Funcionario(models.Model):

    funcionario_id = models.CharField(primary_key=True, default='', max_length=10, unique=True)
    funcionario_nome = models.CharField(max_length=150, default='')
    funcionario_data_nascimento = models.DateField(max_length=10, default='')
    funcionario_endereco = models.CharField(max_length=150, default='')
    funcionario_cpf = models.CharField(max_length=12, default='')
    funcionario_ec = models.CharField(max_length=50, default='')

    def __str__(self):
        return f'Nome: {self.funcionario_nome} | CPF: {self.funcionario_cpf}'
