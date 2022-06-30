from django.contrib.auth.admin import UserAdmin 
from django.contrib import admin

from django.contrib.auth.models import User
from .models import PerfilUsuario


@admin.register(PerfilUsuario)
class PerfilAdmin(admin.ModelAdmin):
    
    list_display = ('pk', 'user')
   
    

class PerfilInLine(admin.StackedInline):
    model = PerfilUsuario
    can_delete = False
    verbose_name_plural = 'perfiles'

class UsuarioAdmin(UserAdmin):
    inlines = (PerfilInLine,)
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_staff'
    )
admin.site.unregister(User)
admin.site.register(User, UsuarioAdmin)