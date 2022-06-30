from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class PerfilUsuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bibliografia = models.TextField(blank=True)

    avatar = models.ImageField(
        upload_to='avatar', 
        blank=True, 
        null=True
    )

    fecha_creacion = models.DateField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.user.username