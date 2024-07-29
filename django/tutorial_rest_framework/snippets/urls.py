from django.urls import path
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('fragmentos/', views.ListarFragmentos.as_view()),
    path('fragmentos/<int:pk>/', views.DetallesFragmentos.as_view()),
    path('usuarios/', views.ListaUsuarios.as_view()),
    path('usuarios/<int:pk>/', views.DetalleUsuario.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)