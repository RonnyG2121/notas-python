# from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from snippets.models import Fragmento
from snippets.serializers import Serializador_fragmento

# Create your views here.


@csrf_exempt
def crear_Fragmento(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializador = Serializador_fragmento(data=data)
        if serializador.is_valid():
            serializador.save()
            return JsonResponse(serializador.data, status=201)
        return JsonResponse(serializador.errors, status=400)


@csrf_exempt
def listar_fragmentos(request):
    """
    Esta vista lista todos los fragmentos de código
    """

    if request.method == 'GET':
        fragmentos = Fragmento.objects.all()
        serializador = Serializador_fragmento(fragmentos, many=True)

        return JsonResponse(serializador.data, safe=False)
    

@csrf_exempt
def listar_un_fragmento(request, pk):
    """
    Esta vista lista un solo fragmento de código
    """

    try:
        fragmento = Fragmento.objects.get(pk=pk)
    except Fragmento.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializador = Serializador_fragmento(fragmento)

        return JsonResponse(serializador.data, safe=False)
    
    return JsonResponse(serializador.errors)


@csrf_exempt
def actualizar_un_fragmento(request, pk):
    """
    Esta vista actualiza un solo fragmento de código
    """

    try:
        fragmento = Fragmento.objects.get(pk=pk)
    except Fragmento.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializador = Serializador_fragmento(fragmento, data=data)

        if serializador.is_valid():
            serializador.save()
            return JsonResponse(serializador.data)

    return JsonResponse(serializador.errors, status=400)


@csrf_exempt
def eliminar_un_fragmento(request, pk):
    """
    Esta vista elimina un solo fragmento de código
    """

    try:
        fragmento = Fragmento.objects.get(pk=pk)
    except Fragmento.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'DELETE':
        fragmento.delete()

        return HttpResponse(status=204)

