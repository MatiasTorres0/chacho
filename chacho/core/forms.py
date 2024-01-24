from django import forms
from django.forms import ModelForm
from .models import JuegoMod, Comando
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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

