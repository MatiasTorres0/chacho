from django import forms
from django.forms import ModelForm
from .models import JuegoMod, Comando
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Ticket

class JuegoModForm(forms.ModelForm):
    class Meta:
        model = JuegoMod
        fields = [
            'nombre_mod','mes', 'nombre_juego'
            
        ]

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
