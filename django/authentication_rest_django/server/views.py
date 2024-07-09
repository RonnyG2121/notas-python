# This is a views from the rest_framework from django

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .serializer import UserSerializer
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404


# Creating routs to api

@api_view(['POST'])
def login(request):
    # Obtener el nombre de usuario de la solicitud
    username = request.data['username']
    password = request.data['password']

    # Buscar el usuario en la base de datos
    user = get_object_or_404(User, username=username)
    # Verificar si el usuario tiene una contraseña y si la contraseña es válida
    if not password:
        return Response({'error': 'La contraseña no fue proporcionada'}, status=status.HTTP_400_BAD_REQUEST)
    if not user.check_password(password):
        return Response({'error': 'Contraseña inválida'}, status=status.HTTP_400_BAD_REQUEST)

    # Crear o recuperar el token para el usuario
    token, created = Token.objects.get_or_create(user=user)

    # Serializar el usuario para devolverlo en json en la respuesta
    user_serializer = UserSerializer(user)

    # Devolver la respuesta
    return Response({"token": token.key, "user": user_serializer.data, "status": status.HTTP_200_OK})


@api_view(['POST'])
def register(request):
    print(request.data)
    user_serializer = UserSerializer(data=request.data)
    if user_serializer.is_valid():
        user_serializer.save()
        user_instance = User.objects.get(username=user_serializer.data['username'])
        user_instance.set_password(request.data['password'])
        user_instance.save()
        my_token = Token.objects.create(user=user_instance)  
        return Response({"token": my_token.key, "user": user_serializer.data, "status": status.HTTP_201_CREATED})
    else:
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes(permission_classes=[IsAuthenticated])
@authentication_classes(authentication_classes=[TokenAuthentication])
def profile(request):
    # Obtener el token del usuario autenticado
    user = request.user
    token = request.auth  # Esto contiene el token del usuario

    # Imprimir el token en la consola
    print(f'Token del usuario: {token}')

    # Responder con algún dato, por ejemplo el nombre de usuario
    return Response({'username': user.username})
