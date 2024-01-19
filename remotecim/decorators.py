from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import redirect
from .settings import ROLES

def administrador_required(view_func):
    def check_administrador(user):
        return user.is_authenticated and user.rol == ROLES['ADMINISTRADOR']
    return user_passes_test(check_administrador)(view_func)

def profesor_required(view_func):
    def check_profesor(user):
        return user.is_authenticated and user.rol == ROLES['PROFESOR']
    return user_passes_test(check_profesor)(view_func)

def estudiante_required(view_func):
    def check_estudiante(user):
        return user.is_authenticated and user.rol == ROLES['ESTUDIANTE']
    return user_passes_test(check_estudiante)(view_func)
