from django.contrib import admin
from .models import Category, Article

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}
    date_hierarchy = 'created_at'
    ordering = ('name',)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'source', 'publication_date', 'created_at')
    list_filter = ('category', 'publication_date', 'created_at')
    search_fields = ('title', 'author', 'summary', 'commentary', 'source', 'url')
    prepopulated_fields = {'slug': ('title', 'author')}
    date_hierarchy = 'created_at'
    raw_id_fields = ('user',)
    autocomplete_fields = ('category',)
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Información básica', {
            'fields': ('user', 'title', 'slug', 'author', 'category')
        }),
        ('Fuente de información', {
            'fields': ('source', 'url', 'publication_date')
        }),
        ('Contenido', {
            'fields': ('summary', 'commentary')
        }),
        ('Metadatos', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
