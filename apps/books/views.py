from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import Book, Genre
from .forms import BookForm, GenreForm

# Capa de servicio / lógica de negocio
class BookService:
    @staticmethod
    def get_books(request):
        """Obtiene todos los libros con paginación"""
        books = Book.objects.all().select_related('genre')
        paginator = Paginator(books, 9)  # 9 libros por página
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return page_obj
    
    @staticmethod
    def get_book_by_slug(slug):
        """Obtiene un libro por su slug"""
        return get_object_or_404(Book, slug=slug)
    
    @staticmethod
    def create_book(book_instance):
        """Crea un nuevo libro"""
        book_instance.save()
        return book_instance
    
    @staticmethod
    def update_book(instance, form):
        """Actualiza un libro existente"""
        book = form.save()
        return book
    
    @staticmethod
    def delete_book(book):
        """Elimina un libro"""
        book.delete()


class GenreService:
    @staticmethod
    def get_genres():
        """Obtiene todos los géneros"""
        return Genre.objects.all()
    
    @staticmethod
    def get_genre_by_slug(slug):
        """Obtiene un género por su slug"""
        return get_object_or_404(Genre, slug=slug)
    
    @staticmethod
    def create_genre(form):
        """Crea un nuevo género"""
        genre = form.save()
        return genre


# Vistas (capa de presentación)
@login_required
def book_list(request):
    """
    Vista para mostrar la lista de libros del usuario actual
    """
    books = Book.objects.filter(user=request.user).order_by('-created_at')
    genres = Genre.objects.all()
    
    # Filtrar por género si se especifica en la URL
    genre_slug = request.GET.get('genre')
    if genre_slug:
        genre = get_object_or_404(Genre, slug=genre_slug)
        books = books.filter(genre=genre)
        
    context = {
        'books': books,
        'genres': genres,
        'active_genre': genre_slug,
    }
    
    return render(request, 'books/book_list.html', context)


@login_required
def book_detail(request, slug):
    """Vista que muestra el detalle de un libro"""
    book = BookService.get_book_by_slug(slug)
    return render(request, 'books/book_detail.html', {'book': book})


@login_required
def book_create(request):
    """Vista para crear un nuevo libro"""
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save(commit=False)
            book.user = request.user
            BookService.create_book(book)
            messages.success(request, '¡Libro creado con éxito!')
            return redirect('books:list')
    else:
        form = BookForm()
    
    return render(request, 'books/book_form.html', {'form': form, 'action': 'Crear'})


@login_required
def book_update(request, slug):
    """Vista para actualizar un libro existente"""
    book = BookService.get_book_by_slug(slug)
    
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            BookService.update_book(book, form)
            messages.success(request, '¡Libro actualizado con éxito!')
            return redirect('books:detail', slug=book.slug)
    else:
        form = BookForm(instance=book)
    
    return render(request, 'books/book_form.html', {'form': form, 'action': 'Editar', 'book': book})


@login_required
def book_delete(request, slug):
    """Vista para eliminar un libro"""
    book = BookService.get_book_by_slug(slug)
    
    if request.method == 'POST':
        BookService.delete_book(book)
        messages.success(request, '¡Libro eliminado con éxito!')
        return redirect('books:list')
    
    return render(request, 'books/book_confirm_delete.html', {'book': book})


@login_required
def genre_list(request):
    """Vista que muestra la lista de géneros"""
    genres = GenreService.get_genres()
    return render(request, 'books/genre_list.html', {'genres': genres})


@login_required
def genre_detail(request, slug):
    """Vista que muestra el detalle de un género y sus libros"""
    genre = GenreService.get_genre_by_slug(slug)
    books = Book.objects.filter(genre=genre)
    return render(request, 'books/genre_detail.html', {'genre': genre, 'books': books})
