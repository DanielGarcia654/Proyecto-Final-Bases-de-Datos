from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('registro/', views.registro, name='registro'),
    path('registro_exitoso/', views.registro_exitoso, name='registro_exitoso'),

    path('comentario/', views.comentario, name='comentario'),
    path('comentario_exitoso/', views.comentario_exitoso, name='comentario_exitoso'),
    path('reserva/', views.reserva, name='reserva'),
]


