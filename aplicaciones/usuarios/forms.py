from django import forms

from django.contrib.auth.models import User


class RegistroForm(forms.Form):
    username = forms.CharField(min_length=4, max_length=20)
    password = forms.CharField(max_length=70, widget=forms.PasswordInput())
    password_comfirm = forms.CharField(max_length=70, widget=forms.PasswordInput())

    nombre = forms.CharField(min_length=3, max_length=30)
    apellido = forms.CharField(min_length=3, max_length=40)

    email = forms.CharField(min_length=6, max_length=50, widget=forms.EmailInput())


    def clean_username(self):
        username = self.cleaned_data['username']
        username_unique = User.objects.filter(username=username).exists()
        if username_unique:
            raise forms.ValidationError('Nombre de usuario ya existente')
        
        return username

    def clean(self):
        data = super().clean()

        password = data['password']
        password_confirm = data['password_confirm']

        if password != password_confirm:
            raise forms.ValidationError('Las contraseñas no coinciden!')

        return data


class PerfilForm(forms.Form):
    bibliografia = forms.CharField(max_length=200, required=True)
    avatar = forms.ImageField()