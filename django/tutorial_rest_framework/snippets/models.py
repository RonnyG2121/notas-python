from django.db import models

from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles



lexers = [item for item in get_all_lexers() if item [1]]
seleccion_lenguajes = sorted([(item[1][0], item[0]) for item in lexers])
seleccion_estilos = sorted([(item, item) for item in get_all_styles()])

# Create your models here.
class Fragmento(models.Model):
    creado = models.DateTimeField(auto_now=True)
    titulo = models.CharField(max_length=255, blank=True, default='')
    codigo = models.TextField()
    lineas = models.BooleanField(default=False)
    lenguaje = models.CharField(choices=seleccion_lenguajes, default='python', max_length=150)
    estilos = models.CharField(choices=seleccion_estilos, default='friendly', max_length=150)
    
    class Meta:
        ordering = ['creado']

