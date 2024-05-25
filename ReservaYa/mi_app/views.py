from django.shortcuts import render, redirect
from .forms import RegistroForm, ReservaForm
from django.http import HttpResponse
from django.utils import timezone
from datetime import datetime


# Crear las vistas aqui
def home(request):
    return render(request, 'reservaciones/home.html')

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registro_exitoso')
        else:
            return HttpResponse(f"Formulario no valido {form.errors}")
    else:
        form = RegistroForm()
    return render(request, 'reservaciones/registro.html', {'form': form})

def registro_exitoso(request):
    return render(request, 'reservaciones/registro_exitoso.html')

def reserva(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            # Combinar fecha y hora
            date = form.cleaned_data['date']
            time = form.cleaned_data['time']
            fecha_hora_reserva = datetime.combine(date, time)
            reservation.fecha_hora_reserva = fecha_hora_reserva
            reservation.save()
            return redirect('reserva_exitosa')
        else:
            return HttpResponse(f"Formulario no valido {form.errors}")
    else:
        form = ReservaForm(initial={'id_cliente': request.user.cliente.id})  # Ejemplo de asignación de cliente logueado
    return render(request, 'reservaciones/reserva.html', {'form': form})
