from django import forms
from django.contrib.auth.forms import UserCreationForm
from mi_banco.models import Usuario  # Tu modelo personalizado

class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = Usuario
        fields = ['first_name', 'last_name', 'dni', 'telefono', 'username', 'email', 'password1', 'password2']
