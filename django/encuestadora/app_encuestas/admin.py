from django.contrib import admin
from .models import Pregunta, Seleccion

# Register your models here.
admin.site.register(Pregunta)

admin.site.register(Seleccion)