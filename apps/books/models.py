from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django.contrib.auth.models import User


class Genre(models.Model):
    """Modelo para representar un género literario"""
    name = models.CharField(max_length=100, unique=True, verbose_name="Nombre")
    slug = models.SlugField(max_length=120, unique=True, verbose_name="Slug")
    description = models.TextField(blank=True, null=True, verbose_name="Descripción")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    class Meta:
        verbose_name = "Género"
        verbose_name_plural = "Géneros"
        ordering = ['name']

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Book(models.Model):
    """Modelo para representar un libro"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="books", verbose_name="Usuario")
    title = models.CharField(max_length=255, verbose_name="Título")
    slug = models.SlugField(max_length=280, unique=True, verbose_name="Slug")
    author = models.CharField(max_length=255, verbose_name="Autor")
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True, related_name="books", verbose_name="Género")
    publication_year = models.PositiveIntegerField(verbose_name="Año de publicación")
    cover_image = models.ImageField(upload_to='books/covers/%Y/%m/', blank=True, null=True, verbose_name="Portada")
    isbn = models.CharField(max_length=20, blank=True, null=True, verbose_name="ISBN")
    summary = models.TextField(verbose_name="Resumen")
    review = models.TextField(verbose_name="Reseña")
    rating = models.PositiveSmallIntegerField(choices=[(i, i) for i in range(1, 6)], verbose_name="Calificación")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    class Meta:
        verbose_name = "Libro"
        verbose_name_plural = "Libros"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.title} - {self.author}"
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.title}-{self.author}")
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('books:detail', kwargs={'slug': self.slug})
