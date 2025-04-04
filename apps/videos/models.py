from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django.contrib.auth.models import User


class VideoCategory(models.Model):
    """Modelo para representar una categoría de videos"""
    name = models.CharField(max_length=100, unique=True, verbose_name="Nombre")
    slug = models.SlugField(max_length=120, unique=True, verbose_name="Slug")
    description = models.TextField(blank=True, null=True, verbose_name="Descripción")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    class Meta:
        verbose_name = "Categoría de Video"
        verbose_name_plural = "Categorías de Videos"
        ordering = ['name']

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Platform(models.Model):
    """Modelo para representar una plataforma de videos"""
    name = models.CharField(max_length=100, unique=True, verbose_name="Nombre")
    slug = models.SlugField(max_length=120, unique=True, verbose_name="Slug")
    website = models.URLField(blank=True, null=True, verbose_name="Sitio web")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    class Meta:
        verbose_name = "Plataforma"
        verbose_name_plural = "Plataformas"
        ordering = ['name']

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Video(models.Model):
    """Modelo para representar un video"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="videos", verbose_name="Usuario")
    title = models.CharField(max_length=255, verbose_name="Título")
    slug = models.SlugField(max_length=280, unique=True, verbose_name="Slug")
    creator = models.CharField(max_length=255, verbose_name="Creador")
    category = models.ForeignKey(VideoCategory, on_delete=models.SET_NULL, null=True, related_name="videos", verbose_name="Categoría")
    platform = models.ForeignKey(Platform, on_delete=models.SET_NULL, null=True, related_name="videos", verbose_name="Plataforma")
    url = models.URLField(blank=True, null=True, verbose_name="URL")
    duration = models.CharField(max_length=20, blank=True, null=True, verbose_name="Duración")
    thumbnail = models.ImageField(upload_to='videos/thumbnails/%Y/%m/', blank=True, null=True, verbose_name="Miniatura")
    summary = models.TextField(verbose_name="Resumen")
    review = models.TextField(verbose_name="Reseña")
    rating = models.PositiveSmallIntegerField(choices=[(i, i) for i in range(1, 6)], verbose_name="Calificación")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    class Meta:
        verbose_name = "Video"
        verbose_name_plural = "Videos"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.title} - {self.creator}"
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.title}-{self.creator}")
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('videos:detail', kwargs={'slug': self.slug})
