from django import forms
from .models import Video, VideoCategory, Platform

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['title', 'creator', 'platform', 'url', 'duration', 'category', 'thumbnail', 'summary', 'review', 'rating']
        widgets = {
            'summary': forms.Textarea(attrs={'rows': 3}),
            'review': forms.Textarea(attrs={'rows': 4}),
            'duration': forms.TextInput(attrs={'placeholder': 'HH:MM:SS'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
        
        # Personalizar algunos campos específicos
        self.fields['url'].widget.attrs.update({'placeholder': 'https://...'})
        
        # Ordenar listas desplegables
        self.fields['category'].queryset = VideoCategory.objects.all().order_by('name')
        self.fields['platform'].queryset = Platform.objects.all().order_by('name')
        
        # Agregar etiquetas vacías
        self.fields['category'].empty_label = "-- Selecciona una categoría --"
        self.fields['platform'].empty_label = "-- Selecciona una plataforma --" 