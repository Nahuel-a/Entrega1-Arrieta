from django import forms
from .models import Categorias, Comentarios, Post


class FormCategoria(forms.ModelForm):
    
    class Meta:
        model = Categorias
        fields = ['nombre']


class FormPost(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ('autor', 'categoria', 'titulo', 'descripcion', 'contenido', 'imagen')


class FormComentario(forms.ModelForm):

    class Meta:
        model = Comentarios
        fields = ['comentario']
