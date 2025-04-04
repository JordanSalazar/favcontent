from django.contrib import admin
from .models import VideoCategory, Platform, Video

# Register your models here.
@admin.register(VideoCategory)
class VideoCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}
    date_hierarchy = 'created_at'
    ordering = ('name',)

@admin.register(Platform)
class PlatformAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'website', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('name', 'website')
    prepopulated_fields = {'slug': ('name',)}
    date_hierarchy = 'created_at'
    ordering = ('name',)

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'creator', 'category', 'platform', 'url', 'duration', 'created_at')
    list_filter = ('category', 'platform', 'created_at')
    search_fields = ('title', 'creator', 'summary', 'review', 'platform', 'url')
    prepopulated_fields = {'slug': ('title', 'creator')}
    date_hierarchy = 'created_at'
    raw_id_fields = ('user',)
    autocomplete_fields = ('category', 'platform')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Información básica', {
            'fields': ('user', 'title', 'slug', 'creator', 'category', 'platform')
        }),
        ('Detalles del video', {
            'fields': ('url', 'duration', 'thumbnail', 'summary', 'review', 'rating')
        }),
        ('Metadatos', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )       