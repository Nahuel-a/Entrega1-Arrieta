from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.db.utils import IntegrityError

from django.contrib.auth.models import User
from .models import PerfilUsuario

# Create your views here.

def inicio_sesion(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('blog:index')
        else:
            return render(request, 'users/login.html',{'error': 'Usuario y contraseña incorrecta'})

    return render(request, 'users/login.html')


def registro(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        password_confirm = request.POST['password_confirm']

        if password != password_confirm:
            return render(request, 'users/register.html',{'error': 'Las contraseñas no coinciden!'})
        
        try:
            user = User.objects.create_user(username=username, password=password)
        except IntegrityError:
            return render(request, 'users/register.html',{'error': 'Nombre de usuario ya existente'})

        user.first_name = request.POST['nombre']
        user.last_name = request.POST['apellido']
        user.email = request.POST['email']
        user.save()

        perfil = PerfilUsuario(user=user)
        perfil.save()

        return redirect('blog:index')
    return render(request, 'users/register.html')


def actualizar_perfil(request):
    return render('users/profile.html')


@login_required
def cerrar_sesion(request):
    logout(request)
    return redirect('blog:index')