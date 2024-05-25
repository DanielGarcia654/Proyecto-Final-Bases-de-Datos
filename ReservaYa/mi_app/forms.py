# forms.py

from django import forms
from .models import Cliente

class RegistroForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre_cliente', 'numero_telefonico', 'correo_electronico']
        labels = {
            'nombre_cliente': 'Nombre',
            'numero_telefonico': 'Teléfono',
            'correo_electronico': 'Correo Electrónico',
        }
