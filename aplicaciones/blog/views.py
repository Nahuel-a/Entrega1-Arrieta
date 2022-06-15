from django.shortcuts import redirect, render
from .models import Post, Autor, Categorias
from .forms import CustomUserCreationForm, FormAutor, FormPost, FormCategoria, UserCreationForm
from django.db.models import Q
from django.core.paginator import Paginator

# Create your views here.

def home(request):
    posts = Post.objects.filter(estado = True)
    
    paginator = Paginator(posts, 2)
    pagina = request.GET.get('page')
    posts = paginator.get_page(pagina) 
    
    return render (request, 'index.html',{'posts':posts})

def detallePost(request, titulo):
    post = Post.objects.get(
        titulo = titulo
    )
    print(post)
    return render(request, 'posts.html', {'detalle_post':post})


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
    
    datos ={
        'form': FormAutor
    }
    if request.method == 'POST':
        autor_form = FormAutor(datos=request.POST)
        if autor_form.is_valid():
            autor_form.save()

            return redirect('blog:index')
        datos['form'] = autor_form

    return render(request, 'formulario_autor.html', datos)

    if request.method == "POST":
        autor_form = FormAutor(request.POST)
        if autor_form.is_valid():
            # datos = mi_formulario.cleaned_data
            # post = Autor(
            #     nombres = datos['nombres'], 
            #     apellido = datos['apellido'],
            #     correo = datos['correo'],
            # )
            autor_form.save()
            return redirect('blog:index')
    else:
        autor_form = FormAutor()

    return render(request, 'formulario_autor.html', {'autor_form':autor_form})

def buscar_autor(request):
    queryset = request.GET.get("buscar")
    autores = Autor.objects.filter(estado = True)

    if queryset:
        autores = Autor.objects.filter(
            Q(nombres__icontains = queryset) |
            Q(apellido__icontains = queryset)
        ).distinct()
    
    return render (request, 'buscar_autor.html', {'autores':autores})

    
def registro(request):
    data = {
        'form':CustomUserCreationForm
    }

    return render(request, 'register.html',data)