from django import forms
from .models import Categorias, Post


class FormCategoria(forms.ModelForm):
    class Meta:
        model = Categorias
        fields = ['nombre']

class FormPost(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ('autor', 'categoria', 'titulo', 'descripcion', 'contenido', 'imagen')
        