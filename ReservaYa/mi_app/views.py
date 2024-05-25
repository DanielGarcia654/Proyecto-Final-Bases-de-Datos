from django.shortcuts import render, redirect
from .forms import RegistroForm
from django.http import HttpResponse

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
