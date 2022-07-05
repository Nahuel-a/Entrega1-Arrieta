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


@login_required
def detallePost(request, pk):
    post = Post.objects.get(id=pk)

    comentarios = Comentarios.objects.filter(comentario_post=post)

    if request.method == 'POST':
        form_comentario=FormComentario(request.POST or None)
        if form_comentario.is_valid():
            contenido=request.POST.get('comentario')
            comentario=Comentarios.objects.create(
                comentario_post=post,
                comentario_autor=request.user,
                comentario=contenido
            )
            comentario.save()
            redirect('blog:index')
    else:
        form_comentario=FormComentario()
    
    context={
            'detalle_post':post,
            'comentarios':comentarios,
            'form_comentario':form_comentario,
        }
    return render(request, 'post/posts.html', context)

def cosplays(request):
    return render (request, 'cosplays.html')

@login_required
def formulario_post(request):

    if request.method == "POST":
        post_form = FormPost(data=request.POST, files=request.FILES)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.autor =request.user
            post.save()

            return render(request, "post/formulario_post.html")
    else:
        post_form = FormPost()

    return render(request, 'post/formulario_post.html', {'post_form':post_form})


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
