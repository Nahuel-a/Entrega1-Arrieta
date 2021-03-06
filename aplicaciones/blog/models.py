from django.db import models
from django.contrib.auth.models import User


class Categorias(models.Model):
    nombre = models.CharField(max_length=40, blank=False, null=False)
    fecha_creacion = models.DateField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.nombre


class Post(models.Model):
    autor = models.ForeignKey(User, on_delete=models.PROTECT)
    titulo = models.CharField(max_length=100, blank=False, null=False)
    descripcion = models.CharField(max_length=255, blank=False, null=False)
    contenido = models.TextField()
    imagen = models.ImageField(upload_to = "post", null=True)  
    fecha_creacion = models.DateField(auto_now=False, auto_now_add=True)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo
    

class Comentarios(models.Model):
    comentario_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comentario_autor = models.ForeignKey(User, on_delete=models.CASCADE)
    comentario = models.TextField()

    fecha_creacion = models.DateField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return 'comentario sobre {} por {}'.format(self.comentario_post.titulo, self.comentario_autor.username)