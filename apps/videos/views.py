from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Video, VideoCategory, Platform
from .forms import VideoForm

# Create your views here.

@login_required
def video_list(request):
    """
    Vista para mostrar la lista de videos del usuario actual
    """
    videos = Video.objects.filter(user=request.user).order_by('-created_at')
    categories = VideoCategory.objects.all()
    platforms = Platform.objects.all()
    
    # Filtrar por categoría si se especifica en la URL
    category_slug = request.GET.get('category')
    if category_slug:
        category = get_object_or_404(VideoCategory, slug=category_slug)
        videos = videos.filter(category=category)
    
    # Filtrar por plataforma si se especifica en la URL
    platform_slug = request.GET.get('platform')
    if platform_slug:
        platform = get_object_or_404(Platform, slug=platform_slug)
        videos = videos.filter(platform=platform)
        
    context = {
        'videos': videos,
        'categories': categories,
        'platforms': platforms,
        'active_category': category_slug,
        'active_platform': platform_slug,
    }
    
    return render(request, 'videos/video_list.html', context)

@login_required
def video_detail(request, slug):
    """Vista que muestra el detalle de un video"""
    video = get_object_or_404(Video, slug=slug, user=request.user)
    return render(request, 'videos/video_detail.html', {'video': video})

@login_required
def video_create(request):
    """Vista para crear un nuevo video"""
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            video = form.save(commit=False)
            video.user = request.user
            video.save()
            messages.success(request, '¡Video creado con éxito!')
            return redirect('videos:detail', slug=video.slug)
    else:
        form = VideoForm()
    
    return render(request, 'videos/video_form.html', {'form': form, 'action': 'Crear'})

@login_required
def video_update(request, slug):
    """Vista para actualizar un video existente"""
    video = get_object_or_404(Video, slug=slug, user=request.user)
    
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES, instance=video)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Video actualizado con éxito!')
            return redirect('videos:detail', slug=video.slug)
    else:
        form = VideoForm(instance=video)
    
    return render(request, 'videos/video_form.html', {
        'form': form, 
        'action': 'Editar',
        'video': video
    })

@login_required
def video_delete(request, slug):
    """Vista para eliminar un video"""
    video = get_object_or_404(Video, slug=slug, user=request.user)
    
    if request.method == 'POST':
        video.delete()
        messages.success(request, '¡Video eliminado con éxito!')
        return redirect('videos:list')
    
    return render(request, 'videos/video_confirm_delete.html', {'video': video})
