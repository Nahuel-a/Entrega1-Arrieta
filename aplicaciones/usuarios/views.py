from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from aplicaciones.usuarios.models import PerfilUsuario

from .forms import RegistroForm, PerfilForm



@login_required
def actualizar_perfil(request):
    if request.method == 'POST':
        form_perfil = PerfilForm(data=request.POST, files=request.FILES)
        if form_perfil.is_valid():
            biografia=request.POST.get('biografia')
            avatar=request.POST.get('avatar')
            perfil=PerfilUsuario.objects.create(
                user=request.user,
                biografia=biografia,
                avatar=avatar
            )
            perfil.save()

            return redirect('account:profile')            
    else:
        form_perfil = PerfilForm()

    return render(
        request=request,
        template_name= 'users/profile.html',
        context= {
            'perfil': form_perfil,
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