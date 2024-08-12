from django.urls import path
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = format_suffix_patterns([
    path('', views.inicio),
    path('fragmento/', views.ListarFragmentos.as_view(), name='lista-fragmento'),
    path('fragmento/<int:pk>/', views.DetallesFragmentos.as_view(), name='detalles-fragmentos'),
    path('fragmento/<int:pk>/resaltado/', views.FragmentoResaltado.as_view(), name='fragmento-resaltado'),
    path('usuario/', views.ListaUsuarios.as_view(), name='lista-usuario'),
    path('usuario/<int:pk>/', views.DetalleUsuario.as_view(), name='detalle-usuario'),
])
