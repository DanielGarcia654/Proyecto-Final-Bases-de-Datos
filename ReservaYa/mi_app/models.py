from django.db import models
from django.utils import timezone

# Create your models here.
class Mesa(models.Model):
    id_mesa = models.AutoField(primary_key=True)
    estado = models.CharField(max_length=30)
    capacidad = models.PositiveIntegerField()

    def __str__(self):
        return f"Mesa {self.id_mesa} - {self.estado}"

class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nombre_cliente = models.CharField(max_length=30)
    numero_telefonico = models.CharField(max_length=13)
    correo_electronico = models.EmailField(max_length=254)
    numero_visitas = models.PositiveIntegerField()

    def __str__(self):
        return self.nombre_cliente

class Reservacion(models.Model):
    id_reservacion = models.AutoField(primary_key=True)
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    id_mesa = models.ForeignKey(Mesa, on_delete=models.CASCADE)
    numero_comensales = models.PositiveIntegerField()
    fecha_hora_reserva = models.DateTimeField()
    tipo_reserva = models.CharField(max_length=30)
    tiempo_estancia_estimado = models.DurationField()

    def __str__(self):
        return f"Reservación {self.id_reservacion} - {self.tipo_reserva}"

class ClienteFrecuente(models.Model):
    id_cliente = models.OneToOneField(Cliente, on_delete=models.CASCADE, primary_key=True)
    preferencias_comidas = models.CharField(max_length=40)
    preferencias_mesa = models.CharField(max_length=40)

    def __str__(self):
        return f"Cliente Frecuente {self.id_cliente.nombre_cliente}"

class ComentarioCalificacion(models.Model):
    id_comentario = models.AutoField(primary_key=True)
    id_reservacion = models.ForeignKey(Reservacion, on_delete=models.CASCADE)
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    comentario = models.TextField(max_length=1000)
    calificacion = models.PositiveIntegerField()

    def __str__(self):
        return f"Comentario {self.id_comentario} - Calificación {self.calificacion}"

class RegistroPagos(models.Model):
    id_registropagos = models.AutoField(primary_key=True)
    id_reservacion = models.ForeignKey(Reservacion, on_delete=models.CASCADE)
    fecha_hora_pago = models.DateTimeField(default=timezone.now)
    monto = models.DecimalField(max_digits=10, decimal_places=4)

    def __str__(self):
        return f"Pago {self.id_registropagos} - Monto {self.monto}"

class HistorialReservaciones(models.Model):
    id_reservacion = models.ForeignKey(Reservacion, on_delete=models.CASCADE, primary_key=True)
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, primary_key=True)
    fecha_hora_visita = models.DateTimeField()
    detalles_reservacion = models.TextField(max_length=1000)

    class Meta:
        unique_together = (('id_reservacion', 'id_cliente'),)

    def __str__(self):
        return f"Historial {self.id_reservacion.id_reservacion} - Cliente {self.id_cliente.nombre_cliente}"
    
    

