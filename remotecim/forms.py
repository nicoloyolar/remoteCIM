from django import forms
from .models import Usuario
from django import forms

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

class GuardarPuntoForm(forms.Form):
    LETRAS_CHOICES = [('A', 'A')]
    NUMEROS_CHOICES = [(str(i), str(i)) for i in range(1, 21)]

    nombre_punto = forms.ChoiceField(choices=LETRAS_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    valor_punto = forms.ChoiceField(choices=NUMEROS_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))