from django import forms

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
