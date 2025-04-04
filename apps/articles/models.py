from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django.contrib.auth.models import User


class Category(models.Model):
    """Modelo para representar una categoría de artículos"""
    name = models.CharField(max_length=100, unique=True, verbose_name="Nombre")
    slug = models.SlugField(max_length=120, unique=True, verbose_name="Slug")
    description = models.TextField(blank=True, null=True, verbose_name="Descripción")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"
        ordering = ['name']

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Article(models.Model):
    """Modelo para representar un artículo"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="articles", verbose_name="Usuario")
    title = models.CharField(max_length=255, verbose_name="Título")
    slug = models.SlugField(max_length=280, unique=True, verbose_name="Slug")
    author = models.CharField(max_length=255, verbose_name="Autor")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name="articles", verbose_name="Categoría")
    source = models.CharField(max_length=255, verbose_name="Fuente")
    url = models.URLField(blank=True, null=True, verbose_name="URL")
    publication_date = models.DateField(blank=True, null=True, verbose_name="Fecha de publicación")
    summary = models.TextField(verbose_name="Resumen")
    commentary = models.TextField(verbose_name="Comentario")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    class Meta:
        verbose_name = "Artículo"
        verbose_name_plural = "Artículos"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.title} - {self.author}"
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.title}-{self.author}")
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('articles:detail', kwargs={'slug': self.slug})
