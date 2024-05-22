from django.shortcuts import render

# Crear las vistas aqui
def home(request):
    return render(request, 'reservaciones/home.html')
