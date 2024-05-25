# forms.py

from django import forms
from .models import Cliente, Reservacion, ComentarioCalificacion

class RegistroForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre_cliente', 'numero_telefonico', 'correo_electronico']
        labels = {
            'nombre_cliente': 'Nombre',
            'numero_telefonico': 'Teléfono',
            'correo_electronico': 'Correo Electrónico',
        }
class ReservaForm(forms.ModelForm):
    date = forms.DateField(label='Fecha (YYYY-MM-DD)', widget=forms.DateInput(attrs={'type': 'date'}))
    time = forms.TimeField(label='Hora (HH:MM  -- p.m/a.m)', widget=forms.TimeInput(attrs={'type': 'time'}))
    
    class Meta:
        model = Reservacion
        fields = ['id_cliente', 'id_mesa', 'numero_comensales', 'tipo_reserva', 'tiempo_estancia_estimado']
        labels = {
            'id_cliente': 'Cliente',
            'id_mesa': 'Mesa',
            'numero_comensales': 'Número de Comensales',
            'tipo_reserva': 'Tipo de Reserva',
            'tiempo_estancia_estimado': 'Tiempo Estimado de Estancia',
        }
        widgets = {
            'id_cliente': forms.HiddenInput(),  # Puedes cambiar esto según sea necesario
            'id_mesa': forms.HiddenInput(),  # Puedes cambiar esto según sea necesario
            'tiempo_estancia_estimado': forms.TextInput(attrs={'placeholder': 'HH:MM:SS'}),
        }

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = ComentarioCalificacion
        fields = ['id_reservacion', 'id_cliente', 'comentario', 'calificacion']
        labels = {
            'id_reservacion': 'Reservación',
            'id_cliente': 'Cliente',
            'comentario': 'Comentario',
            'calificacion': 'Calificación',
        }
