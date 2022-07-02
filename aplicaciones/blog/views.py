from django.shortcuts import redirect, render
from .models import Post
from .forms import FormPost, FormCategoria
from django.db.models import Q
from django.core.paginator import Paginator

# Create your views here.

def home(request):
    posts = Post.objects.filter(estado = True)
    paginator = Paginator(posts, 2)
    pagina = request.GET.get('page')
    posts = paginator.get_page(pagina) 
    
    return render (request, 'post/index.html',{'posts':posts})


def detallePost(request, titulo):
    post = Post.objects.get(
        titulo = titulo
    )

    return render(request, 'post/posts.html', {'detalle_post':post})


def cosplays(request):
    return render (request, 'cosplays.html')


def formulario_post(request):
    post = {
        'form': FormPost
    }
    if request.method == "POST":
        post_form = FormPost(data=request.POST)

        if post_form.is_valid():
                        
            post.save()

            return render(request, "post/formulario_post.html")

    return render(request, 'post/formulario_post.html')


def formulario_categoria(request):
    categoria = {
        'form': FormCategoria
    }
    if request.method == "POST":
        categoria_form = FormCategoria(data=request.POST)
        if categoria_form.is_valid():
            categoria_form.save()
            #mensaje
            return redirect('blog:index')

    return render(request, 'post/formulario_categoria.html', categoria)


def formulario_autor(request):
    autor = {
        'form': FormAutor
    }
    if request.method == 'POST':
        autor_form = FormAutor(data=request.POST)
        if autor_form.is_valid():
            autor_form.save()
            return redirect('blog:index')
            
        autor['form'] = autor_form

    return render(request, 'post/formulario_autor.html', autor)


def buscar_autor(request):
    queryset = request.GET.get("buscar")
    autores = Autor.objects.filter(estado = True)

    if queryset:
        autores = Autor.objects.filter(
            Q(nombres__icontains = queryset) |
            Q(apellido__icontains = queryset)
        ).distinct()
    
    return render (request, 'post/buscar_autor.html', {'autores':autores})