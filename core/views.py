from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from apps.books.models import Book
from apps.articles.models import Article
from apps.videos.models import Video

def home_view(request):
    """
    Vista para la página de inicio.
    Redirecciona a dashboard si el usuario está autenticado.
    """
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, 'base/home.html')

@login_required
def dashboard(request):
    # Obtener contenido reciente
    recent_books = Book.objects.filter(user=request.user).order_by('-created_at')[:5]
    recent_articles = Article.objects.filter(user=request.user).order_by('-created_at')[:5]
    recent_videos = Video.objects.filter(user=request.user).order_by('-created_at')[:5]
    
    # Estadísticas de contenido
    books_count = Book.objects.filter(user=request.user).count()
    articles_count = Article.objects.filter(user=request.user).count()
    videos_count = Video.objects.filter(user=request.user).count()
    total_items = books_count + articles_count + videos_count

    # Calcular porcentajes
    books_percentage = (books_count / total_items * 100) if total_items > 0 else 0
    articles_percentage = (articles_count / total_items * 100) if total_items > 0 else 0
    videos_percentage = (videos_count / total_items * 100) if total_items > 0 else 0
    
    context = {
        'recent_books': recent_books,
        'recent_articles': recent_articles,
        'recent_videos': recent_videos,
        'books_count': books_count,
        'articles_count': articles_count,
        'videos_count': videos_count,
        'total_items': total_items,
        'books_percentage': books_percentage,
        'articles_percentage': articles_percentage,
        'videos_percentage': videos_percentage,
    }
    return render(request, 'base/dashboard.html', context)

@login_required
def search_view(request):
    """
    Vista para la búsqueda global en todos los tipos de contenido.
    """
    query = request.GET.get('q', '')
    content_type = request.GET.get('type', 'all')
    
    books = []
    articles = []
    videos = []
    
    if query:
        # Buscar en libros si el tipo es 'all' o 'books'
        if content_type in ['all', 'books']:
            books = Book.objects.filter(
                Q(user=request.user) &
                (Q(title__icontains=query) | 
                Q(author__icontains=query) | 
                Q(summary__icontains=query) |
                Q(genre__name__icontains=query))
            ).distinct()
        
        # Buscar en artículos si el tipo es 'all' o 'articles'
        if content_type in ['all', 'articles']:
            articles = Article.objects.filter(
                Q(user=request.user) &
                (Q(title__icontains=query) | 
                Q(author__icontains=query) | 
                Q(summary__icontains=query) |
                Q(source__icontains=query) |
                Q(category__name__icontains=query))
            ).distinct()
        
        # Buscar en videos si el tipo es 'all' o 'videos'
        if content_type in ['all', 'videos']:
            videos = Video.objects.filter(
                Q(user=request.user) &
                (Q(title__icontains=query) | 
                Q(director__icontains=query) | 
                Q(summary__icontains=query) |
                Q(platform__icontains=query) |
                Q(genre__name__icontains=query))
            ).distinct()
    
    context = {
        'query': query,
        'books': books,
        'articles': articles,
        'videos': videos,
        'content_type': content_type,
        'has_results': bool(books or articles or videos),
    }
    
    return render(request, 'base/search.html', context) 