from django.urls import path
from .views import *

urlpatterns = [
    path('',home, name='index'),
    path('cosplays/',cosplays, name='cosplays'),
    path('formulario_post/', formulario_post, name='formulario_post'),
    path('formulario_categoria/', formulario_categoria, name='formulario_categoria'),
    path('buscar_autor/', buscar_autor, name='buscar_autor'),
   
    path('<int:id>/', detallePost, name='detalle_post'),
    path('<int:post_id>/', post_comentario, name='post_comentario'),

]