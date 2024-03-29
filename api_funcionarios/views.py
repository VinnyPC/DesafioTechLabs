from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .functions import validaFuncionario
from .models import Funcionario
from .serializers import FuncionarioSerializer

from . import functions as functions

import json


@api_view(['GET'])
def get_funcionarios(request):
    if request.method == 'GET':
        funcionarios = Funcionario.objects.all()
        serializer = FuncionarioSerializer(funcionarios, many=True)
        return Response(serializer.data)

    return Response({'Erro': 'Método HTTP não suportado.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['GET'])
def get_by_nome(request, nome):
    try:
        funcionario = Funcionario.objects.get(funcionario_nome=nome)
    except Funcionario.DoesNotExist:
        return Response({'Erro': 'Funcionário não encontrado, verifique as informações'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = FuncionarioSerializer(funcionario)
        return Response(serializer.data)

    return Response({'Erro': 'Método HTTP não suportado.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['POST'])
def cria_funcionario(request):
    if request.method == 'POST':
        novo_funcionario = request.data
        serializer = FuncionarioSerializer(data=novo_funcionario)

        if serializer.is_valid() and validaFuncionario(novo_funcionario.get('funcionario_cpf'), novo_funcionario.get('funcionario_data_nascimento'), novo_funcionario.get('funcionario_nome'), novo_funcionario.get('funcionario_ec')):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({'Erro': 'Algum campo inválido ou cadastro já existente!'}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'Erro': 'Método HTTP não suportado.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
@api_view(['PUT'])
def atualiza_funcionario(request):
    if request.method == 'PUT':
        funcionario_id = request.data.get('funcionario_id')
        if funcionario_id is not None:
            try:
                funcionario_atualizado = Funcionario.objects.get(pk=funcionario_id)
            except Funcionario.DoesNotExist:
                return Response({'error': 'Funcionário não encontrado.'}, status=status.HTTP_404_NOT_FOUND)
            serializer = FuncionarioSerializer(funcionario_atualizado, data=request.data)
            if serializer.is_valid():
                cpf_atualizado = request.data.get('funcionario_cpf')
                dataNascimento_atualizada = request.data.get('funcionario_data_nascimento')
                nome_atualizado = request.data.get('funcionario_nome')
                endereco_atualizado = request.data.get('funcionario_endereco')
                ec_atualizado = request.data.get('funcionario_ec')

                if functions.validaFuncionario(cpf_atualizado, dataNascimento_atualizada, nome_atualizado, ec_atualizado):
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                else:
                    return Response({'Erro': 'Algum campo inválido!'},  status=status.HTTP_400_BAD_REQUEST)
                serializer.save()
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'Erro': 'ID do funcionário não fornecido.'}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'Erro': 'Método HTTP não suportado.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['DELETE'])
def delete_funcionario(request):
    if request.method == 'DELETE':
        funcionario_id = request.data.get('funcionario_id')
        if funcionario_id is not None:
            try:
                funcionario_delete = Funcionario.objects.get(pk=funcionario_id)
                funcionario_delete.delete()
                return Response(status=status.HTTP_202_ACCEPTED)
            except Funcionario.DoesNotExist:
                return Response({'Erro': 'Funcionário não encontrado'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'Erro': 'ID do Funcionário não fornecido.'}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'Erro': 'Método HTTP não suportado.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)