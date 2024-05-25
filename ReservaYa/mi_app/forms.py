# forms.py

from django import forms
from .models import Cliente, Reservacion, ComentarioCalificacion

class LoginForm(forms.Form):
    name = forms.CharField(max_length=30, label="Nombre")
    email = forms.EmailField(label="Correo electrónico")

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
    class Meta:
        model = Reservacion
        fields = ['id_mesa', 'numero_comensales', 'tipo_reserva', 'tiempo_estancia_estimado']

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
