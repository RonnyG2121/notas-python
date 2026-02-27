# Este es un serializador y se utiliza para convertir objetos a tipos de datos nativos de python, como diccionarios o listas. Luego permite deserializar esto a json y serializarlos a objetos complejos

from django.contrib.auth.models import Group, User
from rest_framework import serializers


class SerializadorUsuario(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class SerializadorGrupo(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = [
            'url',
            'name']
