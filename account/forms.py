from django import forms
from .models import User
from django.contrib.auth.hashers import (
    PBKDF2PasswordHasher,
)

class LoginForm(forms.Form):
    username = forms.CharField(
        label="Usuario",
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': 'Ingrese su usuario'
        })
    )

    password = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(attrs={
            'class': 'form-input',
            'placeholder': 'Ingrese su contraseña'
        })
    )

class CreateUserForm(forms.ModelForm):
    password = forms.CharField(
        label = "Contraseña",
        widget=forms.PasswordInput(attrs={
            'class': 'form-input',
            'placeholder': 'Ingrese una contraseña segura'
        })
    )
    class Meta:
        model = User
        fields = ['username', 'email', 'is_staff']