from django.urls import path
from .views import detalle_pregunta, resultados_pregunta


urlpatterns = [
    path('', detalle_pregunta, name='detalle-pregunta'),
    path('resultados-pregunta/<int:pregunta_id>/', resultados_pregunta, name='resultados-pregunta'),
]