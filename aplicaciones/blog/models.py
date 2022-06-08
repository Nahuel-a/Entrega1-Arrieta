from django.db import models


class Categorias(models.Model):
    nombre = models.CharField(max_length=40, blank=False, null=False)
    fecha_creacion = models.DateField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.nombre


class Autor(models.Model):
    nombres = models.CharField(max_length=100, null=False, blank=False)
    apellido = models.CharField(max_length=100, null=False, blank=False)
    correo = models.EmailField(blank=False, null=False)
    estado = models.BooleanField('Autor Activo/No activo', default=True)
    fecha_creacion = models.DateField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return ("{0}, {1}".format(self.nombres, self.apellido))


class Post(models.Model):
    titulo = models.CharField(max_length=100, blank=False, null=False)
    #slug = models.CharField(max_length=100, blank=False, null=False)
    descripcion = models.CharField(max_length=255, blank=False, null=False)
    contenido = models.TextField()
    # autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    fecha_creacion = models.DateField(auto_now=False, auto_now_add=True)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo
    