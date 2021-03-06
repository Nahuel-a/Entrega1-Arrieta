from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('',home, name='index'),
    path('cosplays/',cosplays, name='cosplays'),
    path('formulario_post/', formulario_post, name='formulario_post'),
    path('formulario_categoria/', formulario_categoria, name='formulario_categoria'),
    path('buscar_autor/', buscar_autor, name='buscar_autor'),
    
    path('editar_post/<int:id>',editar_post,name='editar_post'),
    path('<int:id>',eliminar_post,name='eliminar_post'),


    re_path(r'^post/(?P<pk>\d+)/$', detallePost, name='detalle_post'),

]