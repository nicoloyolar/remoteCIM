from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
from django.contrib.auth import logout
import socket


class ConnectDeviceView(View):
    def get(self, request, device_id):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect(('192.168.0.41', 12345))
            s.sendall(b'estacion1')
        return redirect('main')

class ConnectDevice2View(View):
    def get(self, request, device_id):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect(('192.168.0.42', 12345))
            s.sendall(b'estacion_2')
        return redirect('main')
 
class open(View):
    def get(self, request, device_id):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect(('192.168.0.41', 12345))
            s.sendall(b'open')
        return redirect('main') 
    
class close(View):
    def get(self, request, device_id):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect(('192.168.0.41', 12345))
            s.sendall(b'close')
        return redirect('main') 

class home(View):
    def get(self, request, device_id):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect(('192.168.0.41', 12345))
            s.sendall(b'home')
        return redirect('main')

class ejes(View):
    def get(self, request, device_id):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect(('192.168.0.41', 12345))
            s.sendall(b'ejes')
        return redirect('main') 
    
class xyz(View):
    def get(self, request, device_id):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect(('192.168.0.41', 12345))
            s.sendall(b'xyz')
        return redirect('main')

class con(View):
    def get(self, request, device_id):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect(('192.168.0.41', 12345))
            s.sendall(b'con')
        return redirect('main')

class coff(View):
    def get(self, request, device_id):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect(('192.168.0.41', 12345))
            s.sendall(b'coff')
        return redirect('main')

class modo(View):
    def get(self, request, device_id):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect(('192.168.0.41', 12345))
            s.sendall(b'modo')
        return redirect('main')

@ensure_csrf_cookie
@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse_lazy('home'))  
    return render(request, 'login.html')

def home_view(request):
    if request.user.is_authenticated:
        context = {'user': request.user}
        return render(request, 'home.html', context)
    else:
        return redirect('login')

def main_view(request):
    if request.user.is_authenticated:
        return render(request, 'main.html')
    else:
        return redirect('login')

def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('login')
    else:
        return redirect('login')



