# API - Gerenciamento de Funcionários

API Django para gerenciar informações de funcionários. A API é capaz de registrar, consultar, atualizar e deletar registros de funcionários no banco de dados MySQL de acordo com a necessidade do usuário.


## Banco de dados
| Nome | Tipo     | Descrição                |
| :-------- | :------- | :------------------------- |
| `funcionario_id` | `int AI PK` | Chave primária autoincrementada |
| `funcionario_nome` | `varchar(150)` | Nome do funcionário (Apenas letras) |
| `funcionario_data_nascimento` | `date` | Data de nascimento do funcionário (yyyy-mm-dd) |
| `funcionario_endereco` | `varchar(150)` | Endereço do funcionário |
| `funcionario_cpf` | `varchar(12)` | CPF do funcionário (11 números) |
| `funcionario_ec` | `varchar(50)` | Estado civil do funcionário (Apenas letras)|

# Endpoints

### 📄 Buscar todos os funcionários

Retorna uma lista de todos os funcionários.

```http
  GET /funcionarios/
```

#
### 🔍 Buscar funcionário por nome

Retorna informações sobre sobre os funcionários específicos com base no nome fornecido.

```http
  GET /funcionarios/nome/${nome}
```



#
### 📝 Criar registro de funcionário

Adiciona um novo funcionário. Requer um payload com os dados do funcionário. O ID não é necessário.

```http
  POST /funcionarios/add
```


#
### ✏️ Editar registro

```http
  PUT /funcionarios/update
```

Atualiza as informações de um funcionário existente. Requer um payload com o ID e algum dado atualizado.


💡 Certifique-se de que o CPF contenha exatamente 11 dígitos numéricos, a data de nascimento esteja no formato yyyy-mm-dd, o nome e o estado civil não contenham letras. Caso contrário, a requisição resultará em um erro 400 Bad Request, com detalhes sobre o erro.
#
### 🗑️ Deletar registro

Exclui um funcionário com base no ID fornecido. Requer um payload com o ID do funcionário.

```http
  DELETE /funcionarios/delete
```
```JSON
{
    "funcionario_id": {id}
}
```


## Tecnologias Utilizadas

+ PyCharm(IDE)
+ Python 3.11
+ Django 5.0.2
+ MySQL Workbench
+ Insomnia

## Links:

+ [Documentação Django](https://docs.djangoproject.com/en/5.0/intro/tutorial08/)
+ [Documentação Django Databases](https://docs.djangoproject.com/en/5.0/ref/databases/#mysqlclient)
+ [Documentação Python](https://docs.python.org/pt-br/3/tutorial/)
+ [DescolaDev - Gabriel Freitas](https://www.youtube.com/@DescolaDev)

