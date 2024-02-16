from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Funcionario
from .serializers import FuncionarioSerializer

import json

@api_view(['GET'])
def get_funcionarios(request):

    if request.method == 'GET':
        funcionarios = Funcionario.objects.all()
        serializer = FuncionarioSerializer(funcionarios, many=True)
        return Response(serializer.data)

    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_by_nome (request, nome):
    try:
        funcionario = Funcionario.objects.get(funcionario_nome=nome)
    except Funcionario.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':

        serializer = FuncionarioSerializer(funcionario)
        return Response(serializer.data)