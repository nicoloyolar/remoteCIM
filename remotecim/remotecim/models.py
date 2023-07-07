from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

class UsuarioManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('El campo Email es obligatorio')
        
        email = self.normalize_email(email)
        usuario = self.model(email=email, **extra_fields)
        usuario.set_password(password)
        usuario.save(using=self._db)
        return usuario
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        
        return self.create_user(email, password, **extra_fields)

class Usuario(AbstractBaseUser, PermissionsMixin):
    id_usuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    rol = models.CharField(max_length=255)
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    fecha_hora_inicio = models.DateTimeField(null=True, blank=True)
    fecha_hora_fin = models.DateTimeField(null=True, blank=True)
    
    horario_confirmado = models.BooleanField(default=False)
    
    ultima_estacion = models.CharField(max_length=255, choices=(
        ('almacenamiento', 'Almacenamiento'),
        ('mecanizado', 'Mecanizado'),
        ('control_de_calidad', 'Control de Calidad'),
    ), null=True, blank=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nombre', 'apellido']
    
    objects = UsuarioManager()
    
    def __str__(self):
        return self.email

class EstacionDeTrabajo(models.Model):
    id_estacion = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=255)
    disponibilidad = models.BooleanField(default=True)

    def __str__(self):
        return self.descripcion

class Reserva(models.Model):
    id_reserva = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    estacion = models.ForeignKey(EstacionDeTrabajo, on_delete=models.CASCADE)
    fecha_hora_inicio = models.DateTimeField()
    fecha_hora_fin = models.DateTimeField()

    def __str__(self):
        return f"Reserva #{self.id_reserva}"

class Posicion(models.Model):
    id_posicion = models.AutoField(primary_key=True)
    id_estacion = models.ForeignKey(EstacionDeTrabajo, on_delete=models.CASCADE)
    nombre_posicion = models.CharField(max_length=255)
    coordenadas = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre_posicion

class Rutina(models.Model):
    id_rutina = models.AutoField(primary_key=True)
    id_estacion = models.ForeignKey(EstacionDeTrabajo, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

class PosicionRutina(models.Model):
    id_posicion_rutina = models.AutoField(primary_key=True)
    id_rutina = models.ForeignKey(Rutina, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=255)
    coordenadas = models.CharField(max_length=255)
    orden = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

class Webcam(models.Model):
    id_webcam = models.AutoField(primary_key=True)
    id_estacion = models.ForeignKey(EstacionDeTrabajo, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=255)
    url = models.CharField(max_length=255)

    def __str__(self):
        return self.descripcion

class MonitoreoWebcam(models.Model):
    id_monitoreo = models.AutoField(primary_key=True)
    id_estacion = models.ForeignKey(EstacionDeTrabajo, on_delete=models.CASCADE)
    id_webcam = models.ForeignKey(Webcam, on_delete=models.CASCADE)
    fecha_hora_inicio = models.DateTimeField()
    fecha_hora_fin = models.DateTimeField()

    def __str__(self):
        return f"Monitoreo #{self.id_monitoreo}"
    
class Comando(models.Model):
    id_comando = models.AutoField(primary_key=True)
    id_rutina = models.ForeignKey(Rutina, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=255)
    orden = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

class EstacionRutina(models.Model):
    id_estacion = models.ForeignKey(EstacionDeTrabajo, on_delete=models.CASCADE)
    id_rutina = models.ForeignKey(Rutina, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['id_estacion', 'id_rutina'], name='unique_estacion_rutina')
        ]

    def __str__(self):
        return f"Estacion: {self.id_estacion} - Rutina: {self.id_rutina}"

class RutinaPosicion(models.Model):
    id_rutina = models.ForeignKey(Rutina, on_delete=models.CASCADE)
    id_posicion_rutina = models.ForeignKey(PosicionRutina, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['id_rutina', 'id_posicion_rutina'], name='unique_rutina_posicion')
        ]

    def __str__(self):
        return f"Rutina: {self.id_rutina} - Posicion: {self.id_posicion_rutina}"

class EstacionWebcam(models.Model):
    id_estacion = models.ForeignKey(EstacionDeTrabajo, on_delete=models.CASCADE)
    id_webcam = models.ForeignKey(Webcam, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['id_estacion', 'id_webcam'], name='unique_estacion_webcam')
        ]

    def __str__(self):
        return f"Estacion: {self.id_estacion} - Webcam: {self.id_webcam}"