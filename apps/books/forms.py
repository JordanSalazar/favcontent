from django import forms
from .models import Book, Genre


class GenreForm(forms.ModelForm):
    """Formulario para crear/editar un género de libro"""
    class Meta:
        model = Genre
        fields = ['name', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }


class BookForm(forms.ModelForm):
    """Formulario para crear/editar un libro"""
    class Meta:
        model = Book
        fields = ['title', 'author', 'genre', 'publication_year', 'cover_image', 'isbn', 'summary', 'review', 'rating']
        widgets = {
            'summary': forms.Textarea(attrs={'rows': 4}),
            'review': forms.Textarea(attrs={'rows': 6}),
            'publication_year': forms.NumberInput(attrs={'min': 1800, 'max': 2100}),
        }

    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        self.fields['genre'].queryset = Genre.objects.all().order_by('name')
        self.fields['genre'].empty_label = "Selecciona un género" 