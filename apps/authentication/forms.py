from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import UserProfile


class CustomUserCreationForm(UserCreationForm):
    """Formulario para registrar un nuevo usuario"""
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=False, label="Nombre")
    last_name = forms.CharField(max_length=30, required=False, label="Apellidos")

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Este correo electrónico ya está registrado.')
        return email


class CustomUserChangeForm(UserChangeForm):
    """Formulario para actualizar un usuario existente"""
    password = None

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
        
    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if User.objects.filter(email=email).exclude(username=username).exists():
            raise forms.ValidationError('Este correo electrónico ya está registrado.')
        return email


class UserProfileForm(forms.ModelForm):
    """Formulario para actualizar el perfil de usuario"""
    class Meta:
        model = UserProfile
        fields = ['avatar', 'bio']
        labels = {
            'bio': 'Biografía',
            'avatar': 'Foto de perfil'
        }
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 4}),
        }


# Alias para compatibilidad con versiones anteriores
UserRegisterForm = CustomUserCreationForm
UserUpdateForm = CustomUserChangeForm
ProfileUpdateForm = UserProfileForm 