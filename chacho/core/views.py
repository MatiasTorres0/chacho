from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import pandas as pd
from .forms import JuegoModForm, ComandoForm, ExcelUploadForm, TicketForm
from .models import JuegoMod, Comando, Ticket
from django.contrib.auth import logout

def home(request):
    return render(request, 'core/about.html')

@login_required
def formulario(request):
    form = JuegoModForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('lista_juegos')
    return render(request, "core/formulario.html", {'form': form})

def lista_juegos(request):
    juegos = JuegoMod.objects.all()
    return render(request, 'core/lista_juegos.html', {'juegos': juegos})

@login_required
def comando(request):
    form = ComandoForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('lista_comandos')
    return render(request, "core/comando.html", {'form': form})

def lista_comandos(request):
    comandos = Comando.objects.all()
    return render(request, 'core/lista_comandos.html', {'comandos': comandos})

@login_required
def videos(request):
    return render(request, 'core/videos.html')

def upload_excel(request):
    form = ExcelUploadForm(request.POST or None, request.FILES or None)
    if request.method == 'POST' and form.is_valid():
        excel_file = form.cleaned_data['excel_file']
        df = pd.read_excel(excel_file)

        # Procesar el DataFrame y crear instancias de Comando
        comandos = [
            Comando(
                nombre_comando=row['Nombre del Comando'],
                tipo=row['Tipo Comando'],
                descripcion=row['Descripción'],
                canal=row['Canal']
            )
            for _, row in df.iterrows()
        ]
        Comando.objects.bulk_create(comandos)

        return redirect('lista_comandos')

    return render(request, 'core/upload_excel.html', {'form': form})

def speedtest(request):
    return render(request, 'core/speedtest.html')

def custom_logout(request):
    logout(request)
    return redirect('lista_comandos')

def ticket_list(request):
    tickets = Ticket.objects.all()
    return render(request, 'core/ticket_list.html', {'tickets': tickets})

def ticket_detail(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    return render(request, 'core/ticket_detail.html', {'ticket': ticket})

def create_ticket(request):
    form = TicketForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        ticket = form.save(commit=False)
        ticket.usuario = request.user
        ticket.save()
        return redirect('ticket_list')

    return render(request, 'core/create_ticket.html', {'form': form})
