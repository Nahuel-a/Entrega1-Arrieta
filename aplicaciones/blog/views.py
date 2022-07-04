from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post, Comentarios
from .forms import FormComentario, FormPost, FormCategoria
from django.db.models import Q
from django.core.paginator import Paginator

# Create your views here.

def home(request):
    posts = Post.objects.filter(estado = True)
    paginator = Paginator(posts, 2)
    pagina = request.GET.get('page')
    posts = paginator.get_page(pagina) 
    
    return render (request, 'post/index.html',{'posts':posts})


def detallePost(request, id):
    post = Post.objects.get(id=id)

    comentarios = Comentarios.objects.filter(comentario_post_id=id)
    return render(
        request = request,
        template_name= 'post/posts.html', 
        context={
            'detalle_post':post,
            'comentarios':comentarios,
        }
    )

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



def buscar_autor(request):
    queryset = request.GET.get("buscar")
    autores = Autor.objects.filter(estado = True)

    if queryset:
        autores = Autor.objects.filter(
            Q(nombres__icontains = queryset) |
            Q(apellido__icontains = queryset)
        ).distinct()
    
    return render (request, 'post/buscar_autor.html', {'autores':autores})

@login_required
def post_comentario(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        comentarios = FormComentario(request.POST)
        if comentarios.is_valid():
            nuevo_comentario = comentarios.save(commit=False)
            nuevo_comentario.comentario_post = post
            nuevo_comentario.save()

            return redirect('blog:posts', id=post.id)
    else:
        comentarios = FormComentario()
    
    return render (request, '',{'comentarios':comentarios})
