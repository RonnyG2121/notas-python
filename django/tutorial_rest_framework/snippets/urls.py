from django.urls import path
from snippets import views


urlpatterns = [
    path('fragmentos/', views.listar_fragmentos),
    path('fragmento/<int:pk>/', views.listar_un_fragmento),
    path('actualizar-fragmento/<int:pk>/', views.actualizar_un_fragmento),
    path('eliminar-fragmento/<int:pk>/', views.eliminar_un_fragmento),
]