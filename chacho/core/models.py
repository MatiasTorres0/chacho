# in your models.py
from django.db import models
from django.contrib.auth.models import User
from django.db import models
from uuid import uuid4
from django.db import models
from django.db import models
from django.core.management.base import BaseCommand

from django.db import models

from django.db import models

class Jugador(models.Model):
    TWITCH_CHOICES = [
        ('twitch1', 'Nombre en twitch 1'),
        ('twitch2', 'Nombre en twitch 2'),
        # Agrega más opciones según sea necesario
    ]

    POSICIONES_CHOICES = [
        ('PO', 'Portero'),
        ('DFI', 'Defensa Izquierdo'),
        ('DFC', 'Defensa Central'),
        ('DFD', 'Defensa Derecho'),
        ('MC', 'Centrocampista'),
        ('MCO', 'Centrocampista Ofensivo'),
        ('EI', 'Extremo Izquierdo'),
        ('DC', 'Delantero Centro'),
        ('ED', 'Extremo Derecho'),
        # Agrega más opciones según sea necesario
    ]
    ALINEACION_CHOICES = [
        ('4-5-1 Ataque', '4-5-1 ATAQUE'),
        ('4-1-4-1', '4-1-4-1'),
        ('4-2-3-1 Cerrado', '4-2-3-1 CERRADO'),
        ('4-2-3-1 Amplio', '4-2-3-1 AMPLIO'),
        ('4-5-1 Parejo', '4-5-1 PAREJO'),
        ('4-4-1-1 Medio Campo', '4-4-1-1 MEDIO CAMPO'),
        ('4-4-1-1 Ataque', '4-4-1-1 ATAQUE'),
        ('4-4-2 Contención', '4-4-2 CONTENCIÓN'),
        ('4-4-2 Parejo', '4-4-2 PAREJO'),
        ('4-1-2-1-2 Cerrado', '4-1-2-1-2 CERRADO'),
        ('4-1-2-1-2 Amplio', '4-1-2-1-2 AMPLIO'),
        ('4-2-2-2', '4-2-2-2'),
        ('4-3-1-2', '4-3-1-2'),
        ('4-1-3-2', '4-1-3-2'),
        ('4-3-3 Falso 9', '4-3-3 FALSO 9'),
        ('4-3-3 Ataque', '4-3-3 ATAQUE'),
        ('4-3-3 Defensa', '4-3-3 DEFENSA'),
        ('4-3-3 Contención', '4-3-3 CONTENCIÓN'),
        ('4-3-3 Parejo', '4-3-3 PAREJO'),
        ('4-3-2-1', '4-3-2-1'),
        ('4-2-4', '4-2-4'),
        ('5-4-1 Diamante', '5-4-1 DIAMANTE'),
        ('5-4-1 Parejo', '5-4-1 PAREJO'),
        ('5-2-1-2', '5-2-1-2'),
        ('5-3-2 Contención', '5-3-2 CONTENCIÓN'),
        ('5-2-3', '5-2-3'),
        ('3-1-4-2', '3-1-4-2'),
        ('3-4-1-2', '3-4-1-2'),
        ('3-5-2', '3-5-2'),
        ('3-5-1-1', '3-5-1-1'),
        ('3-4-2-1', '3-4-2-1'),
        ('3-4-3 Parejo', '3-4-3 PAREJO'),
        ('3-4-3 Diamante', '3-4-3 DIAMANTE'),
    ]
    nombre_twitch = models.CharField(max_length=50)
    nombre_equipo = models.CharField(max_length=100)
    alineacion = models.CharField(max_length=20, choices=ALINEACION_CHOICES)

    # Jugadores titulares
    titular_1_posicion = models.CharField(max_length=3, choices=POSICIONES_CHOICES, default='')
    titular_1_nombre = models.CharField(max_length=50, default='')
    titular_1_apellido = models.CharField(max_length=50, default='')
    titular_1_apodo = models.CharField(max_length=50, default='')
    titular_1_numero_camiseta = models.PositiveIntegerField(default=1)
    titular_1_altura = models.FloatField(default=0.0)
    titular_1_peso = models.FloatField(default=0)
    titular_2_posicion = models.CharField(max_length=3, choices=POSICIONES_CHOICES, default='')
    titular_2_nombre = models.CharField(max_length=50, default='')
    titular_2_apellido = models.CharField(max_length=50, default='')
    titular_2_apodo = models.CharField(max_length=50, default='')
    titular_2_numero_camiseta = models.PositiveIntegerField(default=2)
    titular_2_altura = models.FloatField(default=0.0)
    titular_2_peso = models.FloatField(default=0)
    titular_3_posicion = models.CharField(max_length=3, choices=POSICIONES_CHOICES, default='')
    titular_3_nombre = models.CharField(max_length=50, default='')
    titular_3_apellido = models.CharField(max_length=50, default='')
    titular_3_apodo = models.CharField(max_length=50, default='')
    titular_3_numero_camiseta = models.PositiveIntegerField(default=3)
    titular_3_altura = models.FloatField(default=0.0)
    titular_3_peso = models.FloatField(default=0)
    titular_4_posicion = models.CharField(max_length=3, choices=POSICIONES_CHOICES, default='')
    titular_4_nombre = models.CharField(max_length=50, default='')
    titular_4_apellido = models.CharField(max_length=50, default='')
    titular_4_apodo = models.CharField(max_length=50, default='')
    titular_4_numero_camiseta = models.PositiveIntegerField(default=4)
    titular_4_altura = models.FloatField(default=0.0)
    titular_4_peso = models.FloatField(default=0)

    titular_5_posicion = models.CharField(max_length=3, choices=POSICIONES_CHOICES, default='')
    titular_5_nombre = models.CharField(max_length=50, default='')
    titular_5_apellido = models.CharField(max_length=50, default='')
    titular_5_apodo = models.CharField(max_length=50, default='')
    titular_5_numero_camiseta = models.PositiveIntegerField(default=5)
    titular_5_altura = models.FloatField(default=0.0)
    titular_5_peso = models.FloatField(default=0)

    titular_6_posicion = models.CharField(max_length=3, choices=POSICIONES_CHOICES, default='')
    titular_6_nombre = models.CharField(max_length=50, default='')
    titular_6_apellido = models.CharField(max_length=50, default='')
    titular_6_apodo = models.CharField(max_length=50, default='')
    titular_6_numero_camiseta = models.PositiveIntegerField(default=6)
    titular_6_altura = models.FloatField(default=0.0)
    titular_6_peso = models.FloatField(default=0)

    titular_7_posicion = models.CharField(max_length=3, choices=POSICIONES_CHOICES, default='')
    titular_7_nombre = models.CharField(max_length=50, default='')
    titular_7_apellido = models.CharField(max_length=50, default='')
    titular_7_apodo = models.CharField(max_length=50, default='')
    titular_7_numero_camiseta = models.PositiveIntegerField(default=7)
    titular_7_altura = models.FloatField(default=0.0)
    titular_7_peso = models.FloatField(default=0)

    titular_8_posicion = models.CharField(max_length=3, choices=POSICIONES_CHOICES, default='')
    titular_8_nombre = models.CharField(max_length=50, default='')
    titular_8_apellido = models.CharField(max_length=50, default='')
    titular_8_apodo = models.CharField(max_length=50, default='')
    titular_8_numero_camiseta = models.PositiveIntegerField(default=8)
    titular_8_altura = models.FloatField(default=0.0)
    titular_8_peso = models.FloatField(default=0)

    titular_9_posicion = models.CharField(max_length=3, choices=POSICIONES_CHOICES, default='')
    titular_9_nombre = models.CharField(max_length=50, default='')
    titular_9_apellido = models.CharField(max_length=50, default='')
    titular_9_apodo = models.CharField(max_length=50, default='')
    titular_9_numero_camiseta = models.PositiveIntegerField(default=9)
    titular_9_altura = models.FloatField(default=0.0)
    titular_9_peso = models.FloatField(default=0)

    titular_10_posicion = models.CharField(max_length=3, choices=POSICIONES_CHOICES, default='')
    titular_10_nombre = models.CharField(max_length=50, default='')
    titular_10_apellido = models.CharField(max_length=50, default='')
    titular_10_apodo = models.CharField(max_length=50, default='')
    titular_10_numero_camiseta = models.PositiveIntegerField(default=10)
    titular_10_altura = models.FloatField(default=0.0)
    titular_10_peso = models.FloatField(default=0)

    titular_11_posicion = models.CharField(max_length=3, choices=POSICIONES_CHOICES, default='')
    titular_11_nombre = models.CharField(max_length=50, default='')
    titular_11_apellido = models.CharField(max_length=50, default='')
    titular_11_apodo = models.CharField(max_length=50, default='')
    titular_11_numero_camiseta = models.PositiveIntegerField(default=11)
    titular_11_altura = models.FloatField(default=0.0)
    titular_11_peso = models.FloatField(default=0)

    # Jugadores suplentes
    suplente_1_posicion = models.CharField(max_length=3, choices=POSICIONES_CHOICES, default='')
    suplente_1_nombre = models.CharField(max_length=50, default='')
    suplente_1_apellido = models.CharField(max_length=50, default='')
    suplente_1_apodo = models.CharField(max_length=50, default='')
    reserva_1_numero_camiseta = models.PositiveIntegerField(null=False, default='')
    suplente_1_altura = models.FloatField(default=0.0)
    suplente_1_peso = models.FloatField(default=0)
    suplente_2_posicion = models.CharField(max_length=3, choices=POSICIONES_CHOICES, default='')
    suplente_2_nombre = models.CharField(max_length=50, default='')
    suplente_2_apellido = models.CharField(max_length=50, default='')
    suplente_2_apodo = models.CharField(max_length=50, default='')
    suplente_2_numero_camiseta = models.PositiveIntegerField(null=False, default='')
    suplente_2_altura = models.FloatField(default=0.0)
    suplente_2_peso = models.FloatField(default=0)

    suplente_3_posicion = models.CharField(max_length=3, choices=POSICIONES_CHOICES, default='')
    suplente_3_nombre = models.CharField(max_length=50, default='')
    suplente_3_apellido = models.CharField(max_length=50, default='')
    suplente_3_apodo = models.CharField(max_length=50, default='')
    suplente_3_numero_camiseta = models.PositiveIntegerField(null=False, default='')
    suplente_3_altura = models.FloatField(default=0.0)
    suplente_3_peso = models.FloatField(default=0)

    suplente_4_posicion = models.CharField(max_length=3, choices=POSICIONES_CHOICES, default='')
    suplente_4_nombre = models.CharField(max_length=50, default='')
    suplente_4_apellido = models.CharField(max_length=50, default='')
    suplente_4_apodo = models.CharField(max_length=50, default='')
    suplente_4_numero_camiseta = models.PositiveIntegerField(null=False, default='')
    suplente_4_altura = models.FloatField(default=0.0)
    suplente_4_peso = models.FloatField(default=0)

    suplente_5_posicion = models.CharField(max_length=3, choices=POSICIONES_CHOICES, default='')
    suplente_5_nombre = models.CharField(max_length=50, default='')
    suplente_5_apellido = models.CharField(max_length=50, default='')
    suplente_5_apodo = models.CharField(max_length=50, default='')
    suplente_5_numero_camiseta = models.PositiveIntegerField(null=False, default='')
    suplente_5_altura = models.FloatField(default=0.0)
    suplente_5_peso = models.FloatField(default=0)

    suplente_6_posicion = models.CharField(max_length=3, choices=POSICIONES_CHOICES, default='')
    suplente_6_nombre = models.CharField(max_length=50, default='')
    suplente_6_apellido = models.CharField(max_length=50, default='')
    suplente_6_apodo = models.CharField(max_length=50, default='')
    suplente_6_numero_camiseta = models.PositiveIntegerField(null=False, default='')
    suplente_6_altura = models.FloatField(default=0.0)
    suplente_6_peso = models.FloatField(default=0)

    suplente_7_posicion = models.CharField(max_length=3, choices=POSICIONES_CHOICES, default='')
    suplente_7_nombre = models.CharField(max_length=50, default='')
    suplente_7_apellido = models.CharField(max_length=50, default='')
    suplente_7_apodo = models.CharField(max_length=50, default='')
    suplente_7_numero_camiseta = models.PositiveIntegerField(null=False, default='')
    suplente_7_altura = models.FloatField(default=0.0)
    suplente_7_peso = models.FloatField(default=0)

    # Jugadores reservas
    reserva_1_posicion = models.CharField(max_length=3, choices=POSICIONES_CHOICES, default='')
    reserva_1_nombre = models.CharField(max_length=50, default='')
    reserva_1_apellido = models.CharField(max_length=50, default='')
    reserva_1_apodo = models.CharField(max_length=50, default='')
    reserva_1_numero_camiseta = models.PositiveIntegerField(null=False, default=0)


    # O cualquier valor predeterminado apropiado
    reserva_1_altura = models.FloatField(default=0.0)
    reserva_1_peso = models.FloatField(default=0)
    reserva_2_posicion = models.CharField(max_length=3, choices=POSICIONES_CHOICES, default='')
    reserva_2_nombre = models.CharField(max_length=50, default='')
    reserva_2_apellido = models.CharField(max_length=50, default='')
    reserva_2_apodo = models.CharField(max_length=50, default='')
    reserva_2_numero_camiseta = models.PositiveIntegerField(null=False, default=0)

 # O cualquier valor predeterminado apropiado
    reserva_2_altura = models.FloatField(default=0.0)
    reserva_2_peso = models.FloatField(default=0)
    # Agrega los demás campos para los demás suplentes y reservas...

    def __str__(self):
        return f"{self.nombre_equipo} - {self.alineacion}"

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
    asunto = models.CharField(max_length=1000)
    descripcion = models.TextField()
    estado = models.CharField(max_length=20, default='Abierto')
    prioridad = models.CharField(max_length=20, default='Normal')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    respuesta = models.TextField(default='', blank=True, null=True, max_length=1000)
    def __str__(self):
        return self.asunto


