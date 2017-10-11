# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from models import Pessoa
from serializers import PessoaSerializer,UserSerializer
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
import json

def index(request):
    return HttpResponse("View teste")

class GetPessoas(APIView):

    def get(self,request):
        pessoas = Pessoa.objects.all()
        serializer = PessoaSerializer(pessoas,many=True)
        return Response(serializer.data)

    def post(self):
        pass


class CadastroPessoa(APIView):

    def get(self,request):
        serializer = PessoaSerializer(Pessoa.objects.all(),many=True)
        return Response(serializer.data)


    def post(self,request,format=None):
        serializer = PessoaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()


class Login(APIView):

    def get(self,request):
        return Response(status=status.HTTP_200_OK)

    def post(self,request):
        usuario = authenticate(username=request.data['email'],password=request.data['senha'])
        if usuario is not None:
            if usuario.is_active:
                login(request,usuario)
                dadosusuario = {"usuario":unicode(request.user)}
                return Response(dadosusuario,status=status.HTTP_201_CREATED)
        else:
            dados = {'Login nao efetuado':'Usuario ou senha incorretos'}
            return Response(dados,status=status.HTTP_401_UNAUTHORIZED)


