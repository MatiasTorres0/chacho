from django.contrib import admin
from .models import JuegoMod, Comando, Equipo, Tactica, Personaje, Alineacion, Formacion
# Register your models here.

admin.site.register(JuegoMod)
#admin.site.register(tacticas)
admin.site.register(Comando)
admin.site.register(Equipo)