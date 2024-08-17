from django.db import models
from django.utils import timezone
import datetime

# Create your models here.

class Pregunta(models.Model):
    texto_pregunta = models.CharField(max_length=255)
    fecha_publicacion = models.DateTimeField("Fecha de publicación")

    def fue_publicado(self):
        return self.fecha_publicacion >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self) -> str:
        return f"Pregunta {self.id}. {self.texto_pregunta}. Fecha de publicación: {self.fecha_publicacion}"


class Seleccion(models.Model):
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    texto_seleccion = models.CharField(max_length=255)
    votos = models.IntegerField(default=0)

    def __str__(self) -> str:
        return f"Selección {self.id}. {self.texto_seleccion}. Número de votos: {self.votos}"

