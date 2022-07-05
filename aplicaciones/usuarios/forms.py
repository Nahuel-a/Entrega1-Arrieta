from django import forms

from django.contrib.auth.models import User
from .models import PerfilUsuario


class RegistroForm(forms.Form):
    username = forms.CharField(label='Nombre de usuario', min_length=4, max_length=20)
    password = forms.CharField(label='Contraseña',max_length=70, widget=forms.PasswordInput)
    password_confirm = forms.CharField(label='Confirmar contraseña',max_length=70, widget=forms.PasswordInput)

    first_name = forms.CharField(label='Nombre',min_length=3, max_length=30)
    last_name = forms.CharField(label='Apellido',min_length=3, max_length=40)

    email = forms.CharField(label='Correo electronico',min_length=6, max_length=50, widget=forms.EmailInput)


    def clean_username(self):
        username = self.cleaned_data['username']
        username_unique = User.objects.filter(username=username).exists()
        if username_unique:
            raise forms.ValidationError('Nombre de usuario ya existente')
        
        return username

    def clean(self):
        data = super().clean()

        password = data.get('password')
        password_confirm = data.get('password_confirm')

        if password != password_confirm:
            raise forms.ValidationError('Las contraseñas no coinciden!')

        return data

    def save(self):
        data = self.cleaned_data
        data.pop('password_confirm')

        user = User.objects.create_user(**data)
        perfil = PerfilUsuario(user=user)
        perfil.save()


class PerfilForm(forms.Form):
    biografia = forms.CharField( 
        widget=forms.Textarea(
            attrs={
                'class':'form-control',
                'placeholder':'Biografia',
                'rows': 4,
                'cols':60
            }
        )
    )
    avatar = forms.ImageField()