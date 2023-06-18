from django import forms
from .models import Usuario, Posicion

from django import forms
from .models import Posicion

class PosicionForm(forms.ModelForm):
    opciones1 = [('opcion1', 'Opción 1'), ('opcion2', 'Opción 2'), ('opcion3', 'Opción 3')]
    opciones2 = [('opcionA', 'Opción A'), ('opcionB', 'Opción B'), ('opcionC', 'Opción C')]
    
    campo_lista1 = forms.ChoiceField(choices=opciones1)
    campo_lista2 = forms.ChoiceField(choices=opciones2)
    
    class Meta:
        model = Posicion
        fields = ['campo_lista1', 'campo_lista2', 'nombre_posicion', 'coordenadas']

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