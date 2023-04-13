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
from .views import login_view, home_view, main_view, logout_view, ConnectDeviceView, ConnectDevice2View, xyz, open, ejes, close, home, con, coff, modo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_view, name = 'login'),
    path('logout/', logout_view, name = 'logout'),
    path('home/', home_view, name = 'home'),
    path('register/', home_view, name = 'register'),
    path('main/', main_view, name='main'),
    path('connect-device/<str:device_id>/', ConnectDeviceView.as_view(), name='connect_device'),
    path('connect-device/<str:device_id>/', ConnectDevice2View.as_view(), name='connect_device'),
    path('xyz/<str:device_id>/', xyz.as_view(), name='xyz'),
    path('ejes/<str:device_id>/', ejes.as_view(), name='ejes'),
    path('open/<str:device_id>/', open.as_view(), name='open'),
    path('close/<str:device_id>/', close.as_view(), name='close'),
    path('home/<str:device_id>/', home.as_view(), name='home'),
    path('con/<str:device_id>/', con.as_view(), name='con'),
    path('coff/<str:device_id>/', coff.as_view(), name='coff'),
    path('modo/<str:device_id>/', modo.as_view(), name='modo'),
    


]



