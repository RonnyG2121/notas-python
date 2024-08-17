from rest_framework import status, permissions, generics, renderers, viewsets
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django.contrib.auth.models import User
from rest_framework.views import APIView

from snippets.models import Fragmento
from snippets.serializers import Serializador_fragmento, SerializadorUsuario
from snippets.permissions import PropietarioOVisitante

# Create your views here.


@api_view(['GET'])
def inicio(request, format=None):
    return Response(
        {
            'usuario': reverse('lista-usuario', request=request, format=format),
            'fragmento': reverse('lista-fragmento', request=request, format=format)})


class VistaFragmentos(viewsets.ModelViewSet):
    queryset = Fragmento.objects.all()
    serializer_class = Serializador_fragmento
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          PropietarioOVisitante]
    lookup_field = 'pk'

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def resaltador(self, request, *args, **kwargs):
        fragmentos = self.get_object()
        return Response(fragmentos.resaltador)

    def perform_create(self, serializer):
        serializer.save(creador=self.request.user)



class VistaUsuarios(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = SerializadorUsuario


# Aquí inician las vistas antitguamente utilizadas
""" class FragmentoResaltado(generics.GenericAPIView):
    queryset = Fragmento.objects.all()
    renderer_classes = [renderers.StaticHTMLRenderer]

    def get(self, request, *args, **kwargs):
        fragmentos = self.get_object()
        return Response(fragmentos.resaltador)
 """



""" class ListarFragmentos(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          PropietarioOVisitante]
    queryset = Fragmento.objects.all()
    serializer_class = Serializador_fragmento

    def perform_create(self, serializer):
        serializer.save(creador=self.request.user)
 """



""" class DetallesFragmentos(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          PropietarioOVisitante]
    queryset = Fragmento.objects.all()
    serializer_class = Serializador_fragmento
"""



""" class ListaUsuarios(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = SerializadorUsuario

 """


""" class DetalleUsuario(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = SerializadorUsuario


 """


"""
class ListarFragmentos(APIView):
    
    # Obtiene una lista de todos los fragmmentos o crea un fragmento
    
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get(self, request, format=None):
        fragmentos = Fragmento.objects.all()
        serializador_fragmento = Serializador_fragmento(fragmentos, many=True)
        return Response(serializador_fragmento.data)

    def post(self, request, format=None):
        serializador_fragmento = Serializador_fragmento(data=request.data)
        if serializador_fragmento.is_valid():
            serializador_fragmento.save()
            return Response(serializador_fragmento.data, status=status.HTTP_201_CREATED)
        return Response(serializador_fragmento.errors, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        serializer.save(creador=self.request.user)

"""


"""
class DetallesFragmentos(APIView):
    # Recupera, actualiza o elimina fragmentos
    

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get_object(self, pk):
        try:
            return Fragmento.objects.get(pk=pk)
        except Fragmento.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def get(self, request, pk, format=None):
        fragmento = self.get_object(pk)
        serializador_fragmento = Serializador_fragmento(fragmento)
        return Response(serializador_fragmento.data)

    def put(self, request, pk, format=None):
        fragmento = self.get_object(pk)
        serializador_fragmento = Serializador_fragmento(fragmento, data=request.data)
        if serializador_fragmento.is_valid():
            serializador_fragmento.save()
            return Response(serializador_fragmento.data)
        return Response(serializador_fragmento.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        fragmento = self.get_object(pk)
        fragmento.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
"""


""" @api_view(['POST'])
def crear_fragmento(request, format=None):
    if request.method == 'POST':
        serializador = Serializador_fragmento(data=request.data)
        if serializador.is_valid():
            serializador.save()
            return Response(serializador.data, status=status.HTTP_201_CREATED)
    
        return Response(serializador.errors, status=status.HTTP_400_BAD_REQUEST)

 """


""" @api_view(['GET'])
def listar_fragmentos(request, format=None):
    # Esta vista lista todos los fragmentos de código
    

    if request.method == 'GET':
        fragmentos = Fragmento.objects.all()
        serializador = Serializador_fragmento(fragmentos, many=True)
        # perform_create(serializador)
        return Response(serializador.data, status=status.HTTP_200_OK)
 
    return Response(serializador.errors, status=status.HTTP_404_NOT_FOUND)
"""
    

""" @api_view(['GET'])
def listar_un_fragmento(request, pk, format=None):
    
    # Esta vista lista un solo fragmento de código
    

    try:
        fragmento = Fragmento.objects.get(pk=pk)
        serializador_fragmento = Serializador_fragmento(fragmento)
    except Fragmento.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'GET':
        serializador = Serializador_fragmento(fragmento)

        return Response(serializador.data, status=status.HTTP_200_OK)
    
    return Response(serializador.errors, status=status.HTTP_404_NOT_FOUND)
 """
    

"""
@api_view(['PUT'])
def actualizar_un_fragmento(request, pk, format=None):
    # Esta vista actualiza un solo fragmento de código
    

    try:
        fragmento = Fragmento.objects.get(pk=pk)
    except Fragmento.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializador = Serializador_fragmento(fragmento, data=data)

        if serializador.is_valid():
            serializador.save()
            return Response(serializador.data, status=status.HTTP_200_OK)
         
    return Response(serializador.errors, status=status.HTTP_400_BAD_REQUEST)

"""

"""
@api_view(['DELETE'])
def eliminar_un_fragmento(request, pk, format=None):
    # Esta vista elimina un solo fragmento de código


    try:
        fragmento = Fragmento.objects.get(pk=pk)
    except Fragmento.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        fragmento.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    """
