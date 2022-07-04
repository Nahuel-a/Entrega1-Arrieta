from django.contrib import admin
from .models import *

class CategoriaAdmin(admin.ModelAdmin):
    search_fields = ['nombre']
    list_display = ('nombre', 'fecha_creacion')


class PostAdmin(admin.ModelAdmin):
    # search_fields = ["categoria"]
    list_display = ["titulo", "imagen", "fecha_creacion", "estado"]
    list_per_page = 5

admin.site.register(Categorias, CategoriaAdmin)

admin.site.register(Post, PostAdmin) 

admin.site.register(Comentarios)