# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

class Pessoa(models.Model):
    nome= models.CharField(max_length=50) #nome + sobrenome
    telefone = models.CharField(max_length=14) #no formato (xx)xxxxx-xxxx
    usuario = models.ForeignKey(User,unique=True) ##Substituir email e senha por uma foreign key de usuario

    def __str__(self):
        return self.nome

class Professor(Pessoa):
    pass

class Projeto(models.Model):
    professor  = models.ForeignKey(Professor,on_delete=models.CASCADE)
    tema = models.CharField(max_length=500)
    descricao = models.CharField(max_length=2000) ## substituir por mini editor de texto conforme reuniao com andre
    especificacao = models.CharField(max_length=2000) ## substituir por mini editor de texto conforme reuniao com andre

    def __str__(self):
        return self.tema



class Avaliador(Pessoa):
    pass


class Grupo(models.Model):
    nome =  models.CharField(max_length=100) ##nome do grupo
    nomeprojeto = models.CharField(max_length=500) ##nome do projeto
    tema = models.ForeignKey(Projeto,on_delete=models.CASCADE) #alterei o nome do atributo apenas para tornar a leitura do model mais didatica. tema = projeto
    descricao =models.CharField(max_length=1000)

    def __str__(self):
        return self.nome



class Aluno(Pessoa):
    grupo = models.ForeignKey(Grupo,on_delete=models.CASCADE,blank=True,null=True) ##ao inves de implementar a lista de alunos na classe grupo, colocar o grupo no aluno.


class Disciplinas(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=500) #breve descrica, não é a ementa
    carga = models.IntegerField()

    def __str__(self):
        return self.nome


class Etapas(models.Model):
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=1000) #ver se vai ser char field ou mini editor de texto
    previsaoentrega = models.DateField() #verificar se esse é o mais adequado
    especificacao = models.CharField(max_length=1000) #ver se vai ser char field ou mini editor de texto

    def __str__(self):
        return self.nome

class Entregas(models.Model):
    etapa = models.ForeignKey(Etapas,on_delete=models.CASCADE)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    dataentrega = models.DateField()
    informacoes = models.CharField(max_length=1000)

    def __str__(self):
        return self.informacoes #ficou ruim, mas por enquanto deixa assim





class Apresentacao(Etapas):
    pass

class Criterios(models.Model):
    apresentacao = models.ForeignKey(Apresentacao,on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=100)
    peso = models.FloatField()

    def __str__(self):
        return self.nome


class Avaliacao(models.Model):
    etapa = models.ForeignKey(Etapas,on_delete=models.CASCADE)
    avaliador = models.ForeignKey(Avaliador,on_delete=models.CASCADE)
    nota = models.FloatField()

    def __str__(self):
        return self.nota #ficou ruim mas deixa assim por enqunto



class AvaliacaoAluno(Avaliacao):
    aluno = models.ForeignKey(Aluno,on_delete=models.CASCADE)



class AvaliacaoGrupo(Avaliacao):
    grupo = models.ForeignKey(Grupo,on_delete=models.CASCADE)