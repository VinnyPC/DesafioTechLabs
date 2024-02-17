from .models import Funcionario
import re
def validaCPF(cpf):
    # Remove todos os caracteres não numéricos
    cpf_numerico = re.sub(r'\D', '', cpf)

    # Verifica se o CPF tem exatamente 11 dígitos após a remoção dos não numéricos
    if len(cpf_numerico) == 11:
        return True
    else:
        return False