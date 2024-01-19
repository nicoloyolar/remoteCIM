from django.contrib import admin
from .models import Usuario, EstacionDeTrabajo, Reserva, Rutina, PosicionRutina, Webcam, MonitoreoWebcam, Comando, EstacionRutina, RutinaPosicion, EstacionWebcam

admin.site.register(Usuario)
admin.site.register(EstacionDeTrabajo)
admin.site.register(Reserva)
admin.site.register(Rutina)
admin.site.register(PosicionRutina)
admin.site.register(Webcam)
admin.site.register(MonitoreoWebcam)
admin.site.register(Comando)
admin.site.register(EstacionRutina)
admin.site.register(RutinaPosicion)
admin.site.register(EstacionWebcam)