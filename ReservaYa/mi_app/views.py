from django.shortcuts import render, redirect
from .forms import RegistroForm, ReservaForm, ComentarioForm, LoginForm
from django.http import HttpResponse
from django.utils import timezone
from datetime import datetime
from .models import Cliente

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
            date_str = request.POST.get('date')
            time_str = request.POST.get('time')
            date = datetime.strptime(date_str, '%Y-%m-%d').date()
            time = datetime.strptime(time_str, '%H:%M').time()
            fecha_hora_reserva = datetime.combine(date, time)
            reservation.fecha_hora_reserva = fecha_hora_reserva
            # Asignar el cliente logueado
            cliente_id = request.session.get('cliente_id')
            if not cliente_id:
                return HttpResponse("Cliente no logueado")
            reservation.id_cliente = Cliente.objects.get(id=cliente_id)
            reservation.save()
            return redirect('reserva_exitosa')
        else:
            print(form.errors)  # Imprimir errores en la consola para depuración
            return HttpResponse(f"Formulario no válido: {form.errors}")
    else:
        form = ReservaForm()
    return render(request, 'reservaciones/reservacion.html', {'form': form})

def comentario(request):
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('comentario_exitoso')
        else:
            print(form.errors)  # Añade esta línea para imprimir los errores en la consola
            return HttpResponse(f"Formulario no válido: {form.errors}")
    else:
        form = ComentarioForm()
    return render(request, 'reservaciones/comentario.html', {'form': form})

def comentario_exitoso(request):
    return render(request, 'reservaciones/comentario_exitoso.html')

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            try:
                cliente = Cliente.objects.get(nombre_cliente=name, correo_electronico=email)
                # Almacenar el ID del cliente en la sesión
                request.session['cliente_id'] = cliente.id_cliente
                return redirect('login_exitoso')  # Redirigir al home después de iniciar sesión
            except Cliente.DoesNotExist:
                return HttpResponse("Nombre o correo electrónico incorrectos")
    else:
        form = LoginForm()
    return render(request, 'reservaciones/login.html', {'form': form})

def login_exitoso(request):
    return render(request, 'reservaciones/login_exitoso.html')

def test_db_connection(request):
    try:
        clientes = Cliente.objects.all()
        return HttpResponse(f"Conexión exitosa: {clientes}")
    except Exception as e:
        return HttpResponse(f"Error en la conexión: {e}")
