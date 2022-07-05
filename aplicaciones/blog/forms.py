from django import forms
from .models import Categorias, Comentarios, Post


class FormCategoria(forms.ModelForm):
    
    class Meta:
        model = Categorias
        fields = ['nombre']


class FormPost(forms.ModelForm):
    titulo = forms.CharField()
    descripcion = forms.CharField()
    contenido = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class':'form-control',
                'placeholder':'Titulo',
                'rows': 4,
                'cols':60
            }
        )
    )

    imagen = forms.ImageField()

    class Meta:
        model = Post
        fields = ['titulo', 'descripcion', 'contenido', 'imagen']
    

class FormComentario(forms.ModelForm):
    comentario = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class':'form-control',
                'placeholder':'Comenta aqui !',
                'rows': 4,
                'cols':50
            }
        )
    )
    class Meta:
        model = Comentarios
        fields = ['comentario']
