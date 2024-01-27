from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import pandas as pd
from .forms import JuegoModForm, ComandoForm, ExcelUploadForm, TicketForm, EquipoForm
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


@login_required
def equipo(request):
    if request.method == 'POST':
        equipo_form = EquipoForm(request.POST, request.FILES)
        tactica_formset = TacticaFormSet(request.POST, prefix='tacticas')
        formacion_formset = FormacionFormSet(request.POST, prefix='formaciones')
        alineacion_formset = AlineacionFormSet(request.POST, prefix='alineaciones')
        personaje_formset = PersonajeFormSet(request.POST, prefix='personajes')

        if equipo_form.is_valid() and tactica_formset.is_valid() and formacion_formset.is_valid() and alineacion_formset.is_valid() and personaje_formset.is_valid():
            equipo = equipo_form.save()

            for tactica_form in tactica_formset:
                tactica = tactica_form.save(commit=False)
                tactica.equipo = equipo
                tactica.save()

            for formacion_form in formacion_formset:
                formacion = formacion_form.save(commit=False)
                formacion.equipo = equipo
                formacion.save()

            for alineacion_form in alineacion_formset:
                alineacion = alineacion_form.save(commit=False)
                alineacion.equipo = equipo
                alineacion.save()

            for personaje_form in personaje_formset:
                personaje = personaje_form.save(commit=False)
                personaje.equipo = equipo
                personaje.save()

            return redirect('lista_comandos')
    else:
        equipo_form = EquipoForm()
        tactica_formset = TacticaFormSet(prefix='tacticas')
        formacion_formset = FormacionFormSet(prefix='formaciones')
        alineacion_formset = AlineacionFormSet(prefix='alineaciones')
        personaje_formset = PersonajeFormSet(prefix='personajes')

    return render(request, "core/equiposformulario.html", {
        'equipo_form': equipo_form,
        'tactica_formset': tactica_formset,
        'formacion_formset': formacion_formset,
        'alineacion_formset': alineacion_formset,
        'personaje_formset': personaje_formset,
    })