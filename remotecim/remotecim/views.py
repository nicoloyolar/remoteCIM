from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
from django.contrib.auth import logout
from django.contrib.auth.decorators import user_passes_test
from .forms import LoginForm, RegistroForm, PosicionForm
from .models import Usuario, Reserva, EstacionDeTrabajo, Posicion
from .decorators import administrador_required, profesor_required, estudiante_required
from .settings import CONNECTION_IP1, CONNECTION_IP2, CONNECTION_IP3
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import socket
from django.utils import timezone


class ConnectDeviceView(View):
    def get(self, request, device_id):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(5) 
                s.connect((CONNECTION_IP1, 12345))
                s.sendall(b'home')
                estacion = EstacionDeTrabajo.objects.get(id_estacion=device_id)
                estacion.disponibilidad = False
                estacion.save()
        except (socket.timeout, ConnectionError):
            return redirect('main')

        return redirect('main')

class ConnectDevice2View(View):
    def get(self, request, device_id):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((CONNECTION_IP2, 12345))
                s.sendall(b'estacion2')
        except ConnectionError:
            return redirect('main')
        
        return redirect('main')
    
class ConnectDevice3View(View):
    def get(self, request, device_id):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((CONNECTION_IP3, 12345))
                s.sendall(b'estacion3')
        except ConnectionError:
            return redirect('main')
        
        return redirect('main')

class SolicitarHorarioView(View):
    def get(self, request):
        estaciones = EstacionDeTrabajo.objects.all()
        context = {
            'estaciones': estaciones
        }
        return render(request, 'solicitar_horario.html', context)

    def post(self, request):
        fecha_hora_inicio = request.POST.get('fecha_hora_inicio')
        fecha_hora_fin = request.POST.get('fecha_hora_fin')
        
        return redirect('home')

def crear_posicion(request):
    if request.method == 'POST':
        form = PosicionForm(request.POST)
        if form.is_valid():
            nombre_posicion = form.cleaned_data['nombre_punto']
            valor_posicion = form.cleaned_data['valor_punto']
            coordenadas = form.cleaned_data['coordenadas']
            
            posicion = Posicion(nombre_posicion=nombre_posicion, valor_posicion=valor_posicion, coordenadas=coordenadas)
            posicion.save()
            
            return redirect('main')
    else:
        form = PosicionForm()

    return render(request, 'crear_posicion.html', {'form': form})

@ensure_csrf_cookie
@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                user.fecha_hora_inicio = timezone.now()  # Establecer la fecha y hora de inicio de sesión
                user.save()
                return redirect('home')
            else:
                form.add_error(None, 'Credenciales inválidas')
    else:
        form = LoginForm()
    
    return render(request, 'login.html', {'form': form})

def home_view(request):
    if request.user.is_authenticated:
        estaciones = EstacionDeTrabajo.objects.all()
        context = {
            'estaciones': estaciones
        }
        return render(request, 'home.html', context)
    else:
        return redirect('login')

    
def historial_view(request):
    usuarios = Usuario.objects.all() 
    if request.user.is_authenticated:
        nombre = request.user.nombre
        
        if nombre == 'valentina':
            usuarios = Usuario.objects.filter(nombre='valentina')
        else:
            usuarios = Usuario.objects.all()
        
        return render(request, 'historial.html', {'usuarios': usuarios})
    
    else:
        return redirect('login')

def horario_view(request):
    if request.user.is_authenticated:
        estaciones = EstacionDeTrabajo.objects.all()
        context = {
            'estaciones': estaciones
        }
        return render(request, 'home.html', context)
    else:
        return redirect('login')
    
def main_view(request):
    if request.user.is_authenticated:
        usuarios = Usuario.objects.all()
        estaciones = EstacionDeTrabajo.objects.all()
        numeros = list(range(1, 11))
        context = {
            'usuarios':usuarios,
            'estaciones': estaciones,
            'numeros': numeros
        }
        return render(request, 'main.html', context)
    else:
        return redirect('login')

def puntos_view(request):
    
    if request.user.is_authenticated:
        return render(request, 'puntos.html')
    
    else:
        return redirect('login')

def register_view(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            password = form.cleaned_data['password']
            usuario.set_password(password)
            usuario.save()
            return redirect('home')
    else:
        form = RegistroForm()
    
    return render(request, 'registro.html', {'form': form})

def logout_view(request):
    user = request.user
    user.fecha_hora_fin = timezone.now()  # Establecer la fecha y hora de cierre de sesión
    user.save()
    logout(request)
    return redirect('home')

@csrf_exempt
def send_message(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        
        if message is None:  
            message = 'auto'
        
        estacion_ip = CONNECTION_IP1
        estacion_puerto = 12345

        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((estacion_ip, estacion_puerto))
                s.sendall(message.encode())
                response = s.recv(1024)  
                response_message = response.decode() 
                print(f"Respuesta recibida: {response_message}")

            return JsonResponse({'status': 'ok'})
        except ConnectionError:
            return JsonResponse({'status': 'error'})

    return JsonResponse({'status': 'error'})

def users_view(request):
    usuarios = Usuario.objects.all() 
    return render(request, 'vista_usuarios.html', {'usuarios': usuarios})


