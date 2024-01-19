from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver
from django.utils import timezone
from .models import Usuario

@receiver(user_logged_in, sender=Usuario)
def actualizar_fecha_hora_inicio(sender, user, request, **kwargs):
    user.fecha_hora_inicio = timezone.now()
    user.save()

@receiver(user_logged_out, sender=Usuario)
def actualizar_fecha_hora_fin(sender, user, request, **kwargs):
    user.fecha_hora_fin = timezone.now()
    user.save()
