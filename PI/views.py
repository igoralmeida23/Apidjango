# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from models import Pessoa
from serializers import PessoaSerializer,UserSerializer
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
