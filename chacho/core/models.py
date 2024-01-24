# in your models.py
from django.db import models
from django.contrib.auth.models import User
class JuegoMod(models.Model):
    MES_CHOICES = [
        ('enero', 'Enero'),
        ('febrero', 'Febrero'),
        ('marzo', 'Marzo'),
        ('abril', 'Abril'),
        ('mayo', 'Mayo'),
        ('junio', 'Junio'),
        ('julio', 'Julio'),
        ('agosto', 'Agosto'),
        ('septiembre', 'Septiembre'),
        ('octubre', 'Octubre'),
        ('noviembre', 'Noviembre'),
        ('diciembre', 'Diciembre'),
    ]

    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('realizado', 'Realizado'),
    ]

    nombre_mod = models.CharField(max_length=50, default='')
    mes = models.CharField(max_length=20, choices=MES_CHOICES)
    nombre_juego = models.CharField(max_length=100)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='pendiente')

    def __str__(self):
        return f'{self.nombre_juego} - {self.mes} - {self.nombre_mod} - {self.estado}'

#class tacticas(models.Model):
#    Estilo = [
#        ('presión constante', 'Presión constante'),
#        ('presión al toque', 'Presión al toque'),
#        ('equilibrado', 'Equilibrado'),
#    ]

#    estilo = models.CharField(max_length=50, choices=Estilo)


class Comando(models.Model):
    TIPO_COMANDO = [
        ('normal', 'Normal'),
        ('moderador', 'Moderador'),
        ('editor de twitch', 'Editor de Twitch'),
    ]
    CANAL = [
        ('chachoyvt', 'ChachoyVT'),
    ]
    nombre_comando = models.CharField(max_length=50, default='')
    tipo = models.CharField(max_length=50, choices=TIPO_COMANDO)
    descripcion = models.CharField(max_length=500, default='')
    canal = models.CharField(max_length=50, choices=CANAL, default='chachoyvt')  # Selecciona un valor predeterminado adecuado

    def __str__(self):
        return self.nombre_comando


class Ticket(models.Model):
    asunto = models.CharField(max_length=255)
    descripcion = models.TextField()
    estado = models.CharField(max_length=20, default='Abierto')
    prioridad = models.CharField(max_length=20, default='Normal')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.asunto
