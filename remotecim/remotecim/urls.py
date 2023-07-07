"""remotecim URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from .views import crear_posicion, login_view, home_view, historial_view, horario_view, main_view, register_view, logout_view, puntos_view, send_message, users_view, ConnectDeviceView, ConnectDevice2View, ConnectDevice3View, SolicitarHorarioView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_view, name = 'login'),
    path('crear_posicion/', crear_posicion, name='crear_posicion'),
    path('logout/', logout_view, name = 'logout'),
    path('home/', home_view, name = 'home'),
    path('historial/', historial_view, name = 'historial'),
    path('horario/',  SolicitarHorarioView.as_view(), name = 'horario'),
    path('registro/', register_view, name = 'registro'),
    path('vista_usuarios/', users_view, name = 'vista_usuarios'),
    path('main/', main_view, name='main'),
    path('connect-device/<str:device_id>/', ConnectDeviceView.as_view(), name='connect_device'),
    path('connect-device/<str:device_id>/', ConnectDevice2View.as_view(), name='connect_device2'),
    path('connect-device/<str:device_id>/', ConnectDevice3View.as_view(), name='connect_device3'),
    path('puntos/', puntos_view, name='puntos'),
    path('send_message/', send_message, name='send_message'),
    path('solicitar_horario/', SolicitarHorarioView.as_view(), name='solicitar_horario'),
]



