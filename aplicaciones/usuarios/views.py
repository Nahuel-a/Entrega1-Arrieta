from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from aplicaciones.usuarios.models import PerfilUsuario

from .forms import RegistroForm, PerfilForm




def actualizar_perfil(request):
    perfil = PerfilUsuario.objects.get(user = request.user)
    if request.method == 'POST':
        form = PerfilForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data

            perfil.biografia = data['biografia']
            perfil.avatar = data['avatar']
            perfil.save()

            return redirect('account:profile')            
    else:
        form = PerfilForm()

    return render(
        request=request,
        template_name= 'users/profile.html',
        context= {
            'perfil': form,
            'user': request.user,
        }
    )


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
            return redirect('blog:index')
    else:
        form = RegistroForm()
    return render(request, 'users/register.html', {'form':form})


@login_required
def cerrar_sesion(request):
    logout(request)
    return redirect('blog:index')