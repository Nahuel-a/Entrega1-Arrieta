from django.contrib import admin
from .models import *

class CategoriaAdmin(admin.ModelAdmin):
    search_fields = ['nombre']
    list_display = ('nombre', 'fecha_creacion')

class AutorAdmin(admin.ModelAdmin):
    search_fields = ['nombres', 'apellido']
    list_display = ('nombres', 'apellido', 'fecha_creacion')

admin.site.register(Categorias, CategoriaAdmin)
admin.site.register(Autor, AutorAdmin)
admin.site.register(Post) 