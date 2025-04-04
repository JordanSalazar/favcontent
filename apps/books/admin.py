from django.contrib import admin
from .models import Book, Genre

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}
    date_hierarchy = 'created_at'
    ordering = ('name',)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'genre', 'publication_year', 'rating', 'created_at')
    list_filter = ('genre', 'publication_year', 'rating', 'created_at')
    search_fields = ('title', 'author', 'summary', 'review', 'isbn')
    prepopulated_fields = {'slug': ('title', 'author')}
    date_hierarchy = 'created_at'
    raw_id_fields = ('user',)
    autocomplete_fields = ('genre',)
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Información básica', {
            'fields': ('user', 'title', 'slug', 'author', 'genre', 'publication_year')
        }),
        ('Detalles del libro', {
            'fields': ('cover_image', 'isbn', 'summary', 'review', 'rating')
        }),
        ('Metadatos', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
