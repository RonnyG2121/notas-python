from django.db import models

from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight



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
    creador = models.ForeignKey('auth.User', related_name='fragmentos', on_delete=models.CASCADE)
    resaltador = models.TextField()

    def save(self, *args, **kwargs):
        """
        Este método usa la librería pygments para crear un resaltador en html de los fragmentos de código
        """
        lexer = get_lexer_by_name(self.lenguaje)
        lineas = 'table' if self.lineas else False
        opciones = {'titulo': self.titulo} if self.titulo else {}
        formatter = HtmlFormatter(estilos=self.estilos, lineas=lineas,
                                  full=True, **opciones)
        self.resaltador= highlight(self.codigo, lexer, formatter)
        super().save(*args, **kwargs)


    class Meta:
        ordering = ['creado']

