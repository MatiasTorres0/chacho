from django import forms
from django.forms import ModelForm
from .models import JuegoMod, Comando, Equipo, Tactica, Formacion, Alineacion, Personaje
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Ticket
from django.forms import formset_factory

class TacticaForm(forms.ModelForm):
    class Meta:
        model = Tactica
        fields = ['nombre', 'descripcion']

class FormacionForm(forms.ModelForm):
    class Meta:
        model = Formacion
        fields = ['nombre', 'descripcion']

class AlineacionForm(forms.ModelForm):
    class Meta:
        model = Alineacion
        fields = ['nombre', 'descripcion']

class PersonajeForm(forms.ModelForm):
    class Meta:
        model = Personaje
        fields = ['nombre', 'descripcion']

TacticaFormSet = formset_factory(TacticaForm, extra=1)
FormacionFormSet = formset_factory(FormacionForm, extra=1)
AlineacionFormSet = formset_factory(AlineacionForm, extra=1)
PersonajeFormSet = formset_factory(PersonajeForm, extra=1)

class EquipoForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = ['nombre_twitch', 'nombre_equipo', 'imagen_logo', 'seccion']

TacticaFormSet = formset_factory(TacticaForm, extra=1)
FormacionFormSet = formset_factory(FormacionForm, extra=1)
AlineacionFormSet = formset_factory(AlineacionForm, extra=1)
PersonajeFormSet = formset_factory(PersonajeForm, extra=1)


class JuegoModForm(forms.ModelForm):
    class Meta:
        model = JuegoMod
        fields = ['nombre_mod','mes', 'nombre_juego']

class ComandoForm(forms.ModelForm):
    class Meta:
        model = Comando
        fields = [
            'nombre_comando', 'tipo', 'descripcion', 'canal'
        ]

class ExcelUploadForm(forms.Form):
    excel_file = forms.FileField()


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['asunto', 'descripcion']


    

    def clean_descripcion(self):
        descripcion = self.cleaned_data['descripcion']
        if len(descripcion) < 10:
            raise forms.ValidationError('La descripción debe tener al menos 10 caracteres.')
        return descripcion

