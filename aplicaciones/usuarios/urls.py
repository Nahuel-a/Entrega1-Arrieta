from django.urls import path
from .views import *

urlpatterns = [
    path('account/login/', inicio_sesion, name='login'),
    path('account/logout/', cerrar_sesion, name='logout'),
    path('account/register/', registro, name='register'),
    path('account/profile/', actualizar_perfil, name='profile')

]