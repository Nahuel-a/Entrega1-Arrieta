from django.urls import path
from .views import *

urlpatterns = [
    path('',home, name='index'),
    path('cosplays/',cosplays, name='cosplays'),
    path('formulario_post/', formulario_post, name='formulario_post'),
    path('formulario_categoria/', formulario_categoria, name='formulario_categoria'),
    path('formulario_autor/', formulario_autor, name='formulario_autor'),
    path('buscar_autor/', buscar_autor, name='buscar_autor'),
    path('<str:titulo>/', detallePost, name='detalle_post'),
    path('register/', registro, name='registro'),
]