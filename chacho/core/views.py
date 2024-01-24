from django.shortcuts import render
from .forms import JuegoModForm, ComandoForm
from .models import JuegoMod, Comando
from django.contrib.auth.decorators import login_required
import pandas as pd
from django.shortcuts import render, redirect
from .forms import ExcelUploadForm
from .models import Comando

# Create your views here.
def home(request):
    return render(request, 'core/about.html')
@login_required
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

@login_required
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
@login_required
def videos(request):
    return render(request, 'core/videos.html')


def upload_excel(request):
    if request.method == 'POST':
        form = ExcelUploadForm(request.POST, request.FILES)
        if form.is_valid():
            excel_file = request.FILES['excel_file']
            df = pd.read_excel(excel_file)

            # Procesar el DataFrame y crear instancias de Comando
            for index, row in df.iterrows():
                comando_instance = Comando(
                    nombre_comando=row['Nombre del Comando'],
                    tipo=row['Tipo Comando'],
                    descripcion=row['Descripción'],
                    canal=row['Canal']
                )
                comando_instance.save()

            return redirect('lista_comandos')  # Cambia 'lista_comandos' con la URL de tu lista de comandos
    else:
        form = ExcelUploadForm()

    return render(request, 'core/upload_excel.html', {'form': form})
