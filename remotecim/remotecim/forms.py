from django import forms
from .models import Usuario, Posicion

from django import forms
from .models import Posicion



class LoginForm(forms.Form):
    email = forms.EmailField(label = 'Email')
    password = forms.CharField(widget = forms.PasswordInput, label='Contraseña')
        
class RegistroForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    ROLES_CHOICES = (
        ('administrador', 'Administrador'),
        ('profesor', 'Profesor'),
        ('estudiante', 'Estudiante'),
    )
    rol = forms.ChoiceField(choices=ROLES_CHOICES)

    class Meta:
        model = Usuario
        fields = ['nombre', 'apellido', 'email', 'password', 'rol']