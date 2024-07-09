# Estas son las vistas de la api

from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets
from server.api.serializer import SerializadorGrupo, SerializadorUsuario

# Create your views here.

class VistasUsuarios(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = SerializadorUsuario
    permission_classes= [permissions.IsAuthenticated]


class VistasGrupos(viewsets.ModelViewSet):
    queryset = Group.objects.all().order_by('name')
    serializer_class = SerializadorGrupo
    permission_classes= [permissions.IsAuthenticated]

