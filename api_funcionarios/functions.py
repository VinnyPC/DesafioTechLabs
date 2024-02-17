from .models import Funcionario
import re
from datetime import datetime

def validaFuncionario(cpf, data_nascimento):
    def validaCPF(cpf):
        # Remove todos os caracteres não numéricos
        cpf_numerico = re.sub(r'\D', '', cpf)

        # Verifica se o CPF tem exatamente 11 dígitos após a remoção dos não numéricos
        return len(cpf_numerico) == 11

    def validaDataNascimento(data_nascimento):
        try:
            # Tenta converter a string para um objeto datetime
            datetime.strptime(data_nascimento, '%Y-%m-%d')
            return True
        except ValueError:
            # Se a conversão falhar, trata o erro e retorna False
            return False

    # Chama as funções de validação e retorna True apenas se ambas forem válidas
    return validaCPF(cpf) and validaDataNascimento(data_nascimento)