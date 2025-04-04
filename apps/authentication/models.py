from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    """Modelo para extender el usuario estándar de Django"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    bio = models.TextField(blank=True, null=True, verbose_name="Biografía")
    avatar = models.ImageField(upload_to='users/avatars/%Y/%m/', blank=True, null=True, verbose_name="Avatar")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    class Meta:
        verbose_name = "Perfil de Usuario"
        verbose_name_plural = "Perfiles de Usuarios"

    def __str__(self):
        return f"Perfil de {self.user.username}"
