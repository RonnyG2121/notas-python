# Este es un serializador y se utiliza para convertir datos a objetos python

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

