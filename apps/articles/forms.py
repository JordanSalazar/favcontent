from django import forms
from .models import Article, Category


class CategoryForm(forms.ModelForm):
    """Formulario para crear/editar una categoría de artículos"""
    class Meta:
        model = Category
        fields = ['name', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }


class ArticleForm(forms.ModelForm):
    """Formulario para crear/editar un artículo"""
    class Meta:
        model = Article
        fields = ['title', 'author', 'source', 'url', 'publication_date', 'category', 'summary']
        widgets = {
            'publication_date': forms.DateInput(attrs={'type': 'date'}),
            'summary': forms.Textarea(attrs={'rows': 4}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
        
        # Personalizar algunos campos específicos
        self.fields['url'].widget.attrs.update({'placeholder': 'https://...'})
        
        # Agregar nuevas categorías vacías
        self.fields['category'].empty_label = "-- Selecciona una categoría --"

        self.fields['category'].queryset = Category.objects.all().order_by('name') 