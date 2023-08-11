from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import user_passes_test
from .forms import LoginForm, RegistroForm, PosicionForm
from .models import Usuario, Reserva, EstacionDeTrabajo, Posicion
from .decorators import administrador_required, profesor_required, estudiante_required
from .settings import CONNECTION_IP1, CONNECTION_IP2, CONNECTION_IP3, PUERTO_SOCKET
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import socket
from django.utils import timezone


class ConnectDeviceView(View):
    def get(self, request, device_id):
        try:
            ultima_estacion = request.GET.get('ultima_estacion')
            if ultima_estacion:
                usuario = request.user  # Obtener el usuario actual
                usuario.ultima_estacion = ultima_estacion
                usuario.save()
                
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(5)
                s.connect((CONNECTION_IP1, 12345))
                s.sendall(b'home')
                estacion = EstacionDeTrabajo.objects.get(id_estacion=device_id)
                estacion.disponibilidad = False
                estacion.save()
        except (socket.timeout, ConnectionError):
            return render(request, 'home.html', {'error_message': 'No se ha podido realizar la conexión con la estación solicitada. Por favor, inténtalo nuevamente.'})

        return redirect('main')

class ConnectDevice2View(View):
    def get(self, request, device_id):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(5)
                s.connect((CONNECTION_IP2, 12345))
                s.sendall(b'home')
                estacion = EstacionDeTrabajo.objects.get(id_estacion=device_id)
                estacion.disponibilidad = False
                estacion.save()
        except (socket.timeout, ConnectionError):
            return render(request, 'home.html', {'error_message': 'No se ha podido realizar la conexión con la estación solicitada. Por favor, inténtalo nuevamente.'})

        return redirect('home')
    
class ConnectDevice3View(View):
    def get(self, request, device_id):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(5)
                s.connect((CONNECTION_IP3, 12345))
                s.sendall(b'home')
                estacion = EstacionDeTrabajo.objects.get(id_estacion=device_id)
                estacion.disponibilidad = False
                estacion.save()
        except (socket.timeout, ConnectionError):
            return render(request, 'home.html', {'error_message': 'No se ha podido realizar la conexión con la estación solicitada. Por favor, inténtalo nuevamente.'})

        return redirect('home')

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

        usuario = Usuario.objects.create(
            fecha_hora_inicio=fecha_hora_inicio,
            fecha_hora_fin=fecha_hora_fin,
            horario_confirmado=False
        )

        def horario_disponible(usuario):
            fecha_hora_inicio = usuario.fecha_hora_inicio
            fecha_hora_fin = usuario.fecha_hora_fin
            
            horarios_solapados = Usuario.objects.filter(
                fecha_hora_inicio__lt=fecha_hora_fin,
                fecha_hora_fin__gt=fecha_hora_inicio,
                horario_confirmado=True
            ).exists()

            return not horarios_solapados

        if usuario:
            if horario_disponible(usuario):
                messages.success(request, 'La solicitud de horario se ha enviado correctamente.')
            else:
                messages.error(request, 'El horario seleccionado no está disponible.')

            return redirect('home')
        else:
            messages.error(request, 'Ocurrió un error al enviar la solicitud de horario.')
            return redirect('solicitar_horario')
        
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

def guardar_punto_view(request):
    if request.method == 'POST':
        nombre_punto = request.POST.get('nombre_punto')
        valor_punto = request.POST.get('valor_punto')

        if not nombre_punto or not valor_punto:
            return JsonResponse({'error': 'Los campos del formulario deben estar completos.'}, status=400)

        nuevo_punto = Posicion(nombre_posicion=nombre_punto, coordenadas=valor_punto)
        nuevo_punto.save()

        return redirect('main')

    return JsonResponse({'error': 'Método no permitido.'}, status=405)

def mover_punto_view(request):
    if request.method == 'POST':
        nombre_punto = request.POST.get('nombre_punto')
        valor_punto = request.POST.get('valor_punto')

        if not nombre_punto or not valor_punto:
            return JsonResponse({'error': 'Los campos del formulario deben estar completos.'}, status=400)

        return redirect('main')

    return JsonResponse({'error': 'Método no permitido.'}, status=405)

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
        posiciones = Posicion.objects.all()
        estaciones = EstacionDeTrabajo.objects.all()
        numeros = list(range(1, 11))
        context = {
            'posiciones': posiciones,
            'estaciones': estaciones,
            'numeros': numeros
        }
        return render(request, 'main.html', context)
    else:
        return redirect('login')

def puntos_view(request):
    if request.method == 'POST':
        nombre_punto = request.POST.get('nombre_punto')
        valor_punto = request.POST.get('valor_punto')

        if not nombre_punto or not valor_punto:
            return JsonResponse({'error': 'Los campos del formulario deben estar completos.'}, status=400)

        nuevo_punto = Posicion(nombre_posicion=nombre_punto, coordenadas=valor_punto)
        nuevo_punto.save()

    puntos = Posicion.objects.all()
    
    return render(request, 'puntos.html', {'puntos': puntos})

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
def send_message_validada(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        
        if message is None:  
            message = 'auto'
        
        estacion_ip = CONNECTION_IP1
        estacion_puerto = PUERTO_SOCKET

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


