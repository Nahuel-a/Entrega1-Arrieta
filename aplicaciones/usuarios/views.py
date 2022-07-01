from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import RegistroForm


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
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('blog:index')
    else:
        form = RegistroForm()
    return render(request, 'users/register.html', {'form':form})


def actualizar_perfil(request):
    
    return render('users/profile.html')


@login_required
def cerrar_sesion(request):
    logout(request)
    return redirect('blog:index')