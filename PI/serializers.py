from rest_framework import serializers
from .models import Pessoa
from django.contrib.auth.models import User

class PessoaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pessoa
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username','password')