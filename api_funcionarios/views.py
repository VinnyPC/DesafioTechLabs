from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

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

    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_by_nome(request, nome):
    try:
        funcionario = Funcionario.objects.get(funcionario_nome=nome)
    except Funcionario.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = FuncionarioSerializer(funcionario)
        return Response(serializer.data)

    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def gerencia_funcionario(request):
    if request.method == 'POST':
        novo_funcionario = request.data
        serializer = FuncionarioSerializer(data=novo_funcionario)

        if serializer.is_valid():
            if functions.validaCPF(novo_funcionario.get('funcionario_cpf')):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response({'error': 'CPF deve ter 11 digitos e não deve ter letras'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'Usuário não é válido'}, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        funcionario_id = request.data.get('funcionario_id')
        if funcionario_id is not None:
            try:
                funcionario_atualizado = Funcionario.objects.get(pk=funcionario_id)
            except Funcionario.DoesNotExist:
                return Response({'error': 'Funcionário não encontrado.'}, status=status.HTTP_404_NOT_FOUND)
            serializer = FuncionarioSerializer(funcionario_atualizado, data=request.data)
            if serializer.is_valid():
                cpf_atualizado = request.data.get('funcionario_cpf')
                if functions.validaCPF(cpf_atualizado):
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                else:
                    return Response({'error': 'CPF deve ter 11 digitos e não deve ter letras'},
                                    status=status.HTTP_400_BAD_REQUEST)
                serializer.save()
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'ID do funcionário não fornecido.'}, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        funcionario_id = request.data.get('funcionario_id')
        if funcionario_id is not None:
            try:
                funcionario_delete = Funcionario.objects.get(pk=funcionario_id)
                funcionario_delete.delete()
                return Response(status=status.HTTP_202_ACCEPTED)
            except Funcionario.DoesNotExist:
                return Response({'error': 'Funcionário não encontrado'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'error': 'ID do funcionário não fornecido.'}, status=status.HTTP_400_BAD_REQUEST)

    return Response({'error': 'Método HTTP não suportado.'}, status=status.HTTP_400_BAD_REQUEST)