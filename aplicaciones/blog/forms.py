from django import forms

class FormCategoria(forms.Form):
    nombre = forms.CharField(max_length=100)


class FormAutor(forms.Form):
    nombres = forms.CharField(max_length=100)
    apellido = forms.CharField(max_length=100)
    correo = forms.EmailField()


class FormPost(forms.Form):
    titulo = forms.CharField(max_length=100)
    #slug = forms.CharField(max_length=100)
    descripcion = forms.CharField(max_length=100)
    contenido = forms.CharField(widget=forms.Textarea)

    