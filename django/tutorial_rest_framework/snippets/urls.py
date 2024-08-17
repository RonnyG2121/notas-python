from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import renderers
from . import views



# Creando múltiples vistas partiendo desde una sola vista viewset y proporcionando las acctiones necesarias a los métodos
lista_Fragmentos = views.VistaFragmentos.as_view({
    'get': 'list',
    'post': 'create'
})
detalles_fragmento = views.VistaFragmentos.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
fragmento_resaltado = views.VistaFragmentos.as_view({
    'get': 'resaltador'
}, renderer_classes=[renderers.StaticHTMLRenderer])
lista_usuarios = views.VistaUsuarios.as_view({
    'get': 'list'
})
detalles_usuario = views.VistaUsuarios.as_view({
    'get': 'retrieve'
})

# Usando enrrutadores para diseñar las url de manera específica
router = DefaultRouter()
router.register(r'fragmentos', views.VistaFragmentos, basename='fragmento')
router.register(r'usuarios', views.VistaUsuarios, basename='usuario')

urlpatterns = [
    path('', include(router.urls)),
    # path('', views.inicio),
    # path('fragmento/', views.ListarFragmentos.as_view(), name='lista-fragmento'),
    # path('fragmento/<int:pk>/', views.DetallesFragmentos.as_view(), name='detalles-fragmentos'),
    # path('fragmento/<int:pk>/resaltado/', views.FragmentoResaltado.as_view(), name='fragmento-resaltado'),
    # path('usuario/', views.ListaUsuarios.as_view(), name='lista-usuario'),
    # path('usuario/<int:pk>/', views.DetalleUsuario.as_view(), name='detalle-usuario'),
]
