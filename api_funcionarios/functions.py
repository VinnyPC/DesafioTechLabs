from .models import Funcionario
import re
from datetime import datetime

def validaFuncionario(cpf, data_nascimento, nome, ec):
    def validaCPF(cpf):
        cpf_numerico = re.sub(r'\D', '', cpf)
        return len(cpf_numerico) == 11

    def validaDataNascimento(data_nascimento):
        try:
            datetime.strptime(data_nascimento, '%Y-%m-%d')
            return True
        except ValueError:
            return False

    def validaNome(nome):
        return not any(char.isdigit() for char in nome)

    def validaEc(ec):
        return not any(char.isdigit() for char in ec)

    return validaCPF(cpf) and validaDataNascimento(data_nascimento) and validaNome(nome) and validaEc(ec)

