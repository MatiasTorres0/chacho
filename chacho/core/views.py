from django.shortcuts import render
from .forms import JuegoModForm, ComandoForm
from .models import JuegoMod, Comando
# Create your views here.
def home(request):
    return render(request, 'core/about.html')

def formulario(request):
    data = {"form": JuegoModForm()}
    if request.method == 'POST':
        formulario = JuegoModForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Guardado Correctamente"
    return render(request, "core/formulario.html", data)

def lista_juegos(request):
    juegos = JuegoMod.objects.all()
    return render(request, 'core/lista_juegos.html', {'juegos': juegos})


def comando(request):
    data = {"form": ComandoForm()}
    if request.method == 'POST':
        Comando = ComandoForm(request.POST)
        if Comando.is_valid():
            Comando.save()
            data['mensaje'] = "Guardado Correctamente"
    return render(request, "core/comando.html", data)

def lista_comandos(request):
    comandos = Comando.objects.all()
    return render(request, 'core/lista_comandos.html', {'comandos': comandos})

def videos(request):
    return render(request, 'core/videos.html')