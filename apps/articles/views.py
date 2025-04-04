from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Article, Category
from .forms import ArticleForm

# Create your views here.

@login_required
def article_list(request):
    """
    Vista para mostrar la lista de artículos del usuario actual
    """
    articles = Article.objects.filter(user=request.user).order_by('-created_at')
    categories = Category.objects.all()
    
    # Filtrar por categoría si se especifica en la URL
    category_slug = request.GET.get('category')
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        articles = articles.filter(category=category)
        
    context = {
        'articles': articles,
        'categories': categories,
        'active_category': category_slug,
    }
    
    return render(request, 'articles/article_list.html', context)

@login_required
def article_detail(request, slug):
    """Vista que muestra el detalle de un artículo"""
    article = get_object_or_404(Article, slug=slug, user=request.user)
    return render(request, 'articles/article_detail.html', {'article': article})

@login_required
def article_create(request):
    """Vista para crear un nuevo artículo"""
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            messages.success(request, '¡Artículo creado con éxito!')
            return redirect('articles:detail', slug=article.slug)
    else:
        form = ArticleForm()
    
    return render(request, 'articles/article_form.html', {'form': form, 'action': 'Crear'})

@login_required
def article_update(request, slug):
    """Vista para actualizar un artículo existente"""
    article = get_object_or_404(Article, slug=slug, user=request.user)
    
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Artículo actualizado con éxito!')
            return redirect('articles:detail', slug=article.slug)
    else:
        form = ArticleForm(instance=article)
    
    return render(request, 'articles/article_form.html', {
        'form': form, 
        'action': 'Editar',
        'article': article
    })

@login_required
def article_delete(request, slug):
    """Vista para eliminar un artículo"""
    article = get_object_or_404(Article, slug=slug, user=request.user)
    
    if request.method == 'POST':
        article.delete()
        messages.success(request, '¡Artículo eliminado con éxito!')
        return redirect('articles:list')
    
    return render(request, 'articles/article_confirm_delete.html', {'article': article})
