from django.http import HttpResponse
from django.shortcuts import render
from .models import Post, Autor, Categorias
from .forms import FormAutor, FormPost, FormCategoria

# Create your views here.

def home(request):
    posts = Post.objects.filter(estado = True)
    return render (request, 'index.html',{'posts':posts})


def cosplays(request):
    return render (request, 'cosplays.html')


def formulario_post(request):
    if request.method == "POST":
        mi_formulario = FormPost(request.POST)

        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            post = Post(
                titulo = datos['titulo'], 
                
                descripcion = datos['descripcion'],
                contenido = datos['contenido'],
            )
            post.save()

            return render(request, "formulario_post.html")

    return render(request, 'formulario_post.html')

def formulario_categoria(request):
    if request.method == "POST":
        mi_formulario = FormCategoria(request.POST)

        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            post = Categorias(
                nombre = datos['nombre'], 
            )
            post.save()

            return render(request, "formulario_categoria.html")

    return render(request, 'formulario_categoria.html')

def formulario_autor(request):
    if request.method == "POST":
        mi_formulario = FormAutor(request.POST)

        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            post = Autor(
                nombre = datos['nombre'], 
                apellido = datos['apellido'],
                correo = datos['correo'],
            )
            post.save()

            return render(request, "formulario_autor.html")

    return render(request, 'formulario_autor.html')


def buscar_autor(request):

    if request.GET['nombre']:
        nombre = request.GET['nombre']
        autores = Autor.objects.filter(nombre__icontains = nombre)
        return render(request, "buscar_autor.html", {"autor": autores})
    else:
        return HttpResponse("Campo vacio")

