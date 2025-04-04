from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import UserProfile
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, UserProfileForm, CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from apps.books.models import Book
from apps.articles.models import Article
from apps.videos.models import Video


def register(request):
    """Vista para el registro de usuarios"""
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Crear un perfil para el usuario
            UserProfile.objects.create(user=user)
            # Iniciar sesión automáticamente
            login(request, user)
            messages.success(request, '¡Cuenta creada con éxito!')
            return redirect('dashboard')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'authentication/register.html', {'form': form})


def user_login(request):
    """Vista para el inicio de sesión"""
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'¡Bienvenido de nuevo, {username}!')
                return redirect('dashboard')
    else:
        form = AuthenticationForm()
    
    return render(request, 'authentication/login.html', {'form': form})


@login_required
def profile(request):
    """Vista para el perfil de usuario"""
    # Obtener conteo de elementos
    books_count = Book.objects.count()
    articles_count = Article.objects.count()
    videos_count = Video.objects.count()
    
    # Calcular porcentajes
    total_items = books_count + articles_count + videos_count
    books_percentage = (books_count / total_items * 100) if total_items > 0 else 0
    articles_percentage = (articles_count / total_items * 100) if total_items > 0 else 0
    videos_percentage = (videos_count / total_items * 100) if total_items > 0 else 0
    
    if request.method == 'POST':
        user_form = CustomUserChangeForm(request.POST, instance=request.user)
        
        # Obtener o crear perfil
        profile, created = UserProfile.objects.get_or_create(user=request.user)
        profile_form = UserProfileForm(request.POST, request.FILES, instance=profile)
        
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            
            # Procesar eliminación de avatar si está marcado
            if request.POST.get('delete_avatar') and profile.avatar:
                profile.avatar.delete()
                profile.avatar = None
                profile.save()
            
            messages.success(request, '¡Perfil actualizado con éxito!')
            return redirect('auth:profile')
    else:
        user_form = CustomUserChangeForm(instance=request.user)
        
        # Obtener o crear perfil
        profile, created = UserProfile.objects.get_or_create(user=request.user)
        profile_form = UserProfileForm(instance=profile)
    
    # Simular actividad reciente
    recent_activities = [
        {
            'content_type': 'book',
            'message': 'Has añadido un nuevo libro: "El nombre del viento"',
            'created_at': '2023-06-01 15:30'
        },
        {
            'content_type': 'article',
            'message': 'Has actualizado el artículo: "Inteligencia Artificial en 2023"',
            'created_at': '2023-05-29 10:15'
        },
        {
            'content_type': 'video',
            'message': 'Has eliminado el video: "Tutorial de Django"',
            'created_at': '2023-05-27 18:45'
        },
    ]
    
    context = {
        'user_form': user_form,
        'profile_form': profile_form,
        'books_count': books_count,
        'articles_count': articles_count,
        'videos_count': videos_count,
        'books_percentage': round(books_percentage),
        'articles_percentage': round(articles_percentage),
        'videos_percentage': round(videos_percentage),
        'recent_activities': recent_activities
    }
    
    return render(request, 'authentication/profile.html', context)


@login_required
def edit_profile(request):
    """Vista para editar el perfil del usuario"""
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, '¡Tu perfil ha sido actualizado!')
            return redirect('auth:profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'authentication/edit_profile.html', context)
