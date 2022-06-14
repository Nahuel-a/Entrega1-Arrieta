from django import forms
from .models import Autor

class FormCategoria(forms.Form):
    nombre = forms.CharField(max_length=100)


class FormAutor(forms.Form):
   class Meta:
        model = Autor
        fields = ['nombres', 'apellido', 'email']


class FormPost(forms.Form):
    titulo = forms.CharField(max_length=100)
    descripcion = forms.CharField(max_length=100)
    contenido = forms.CharField(widget=forms.Textarea)

    