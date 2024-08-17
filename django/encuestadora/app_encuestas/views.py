from django.shortcuts import render, HttpResponse
from .models import Pregunta

# Create your views here.
def detalle_pregunta(request, pregunta_id):
    pregunta = Pregunta.objects.filter(id=pregunta_id)

    return HttpResponse(f"Estás viendo la pregunta {pregunta_id}. {pregunta}")

def resultados_pregunta(request, pregunta_id):
    pregunta = Pregunta.objects.get(id=pregunta_id)
    votos_pregunta = pregunta.seleccion__set.get(votos='votos')

    return HttpResponse(f"Resultados de la pregunta {pregunta_id}. Número de votos: {votos_pregunta}")