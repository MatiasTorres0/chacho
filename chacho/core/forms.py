from django import forms
from django.forms import ModelForm, formset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Ticket, Jugador, Comando, JuegoMod
from django import forms
from .models import Jugador


from django import forms
from .models import Jugador

class JugadorForm(forms.ModelForm):
    class Meta:
        model = Jugador
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        nombre_completo = cleaned_data['nombre'] + ' ' + cleaned_data['apellido']
        if len(nombre_completo) < 10:
            raise forms.ValidationError('El nombre completo debe tener al menos 10 caracteres.')
        return cleaned_data

class ComandoForm(forms.ModelForm):
    class Meta:
        model = Comando
        fields = ['nombre_comando', 'tipo', 'descripcion', 'canal']

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


class JuegoModForm(forms.ModelForm):
    class Meta:
        model = JuegoMod
        fields = ['nombre_mod', 'mes', 'nombre_juego']


class JugadorForm(forms.ModelForm):
    class Meta:
        model = Jugador
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        nombre_completo = cleaned_data['nombre'] + ' ' + cleaned_data['apellido']
        if len(nombre_completo) < 10:
            raise forms.ValidationError('El nombre completo debe tener al menos 10 caracteres.')

        # Validación personalizada para la fecha de nacimiento
        fecha_nacimiento = cleaned_data['fecha_nacimiento']
        if fecha_nacimiento is not None:
            if fecha_nacimiento > datetime.date.today():
                raise forms.ValidationError('La fecha de nacimiento no puede ser posterior a la fecha actual.')

        return cleaned_data