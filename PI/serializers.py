from rest_framework import serializers
from .models import Pessoa
from django.contrib.auth.models import User, UserManager

class PessoaSerializer(serializers.ModelSerializer):


    class Meta:
        model = Pessoa
        fields = ('nome','telefone','email','senha')


    def create(self, validated_data):
        usuario = User.objects.create_user(username=validated_data["email"])
        usuario.username = validated_data["email"]
        usuario.set_password(validated_data["senha"])
        usuario.save()
        pessoa = Pessoa.objects.create(usuario=usuario)
        pessoa.nome = validated_data["nome"]
        pessoa.telefone = validated_data["telefone"]
        pessoa.save()
        return pessoa


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username','password')

