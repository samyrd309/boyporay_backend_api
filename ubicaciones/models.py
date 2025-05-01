from django.db import models
from usuarios.models import Conductor

# Create your models here.

class UltimaUbicacionAutobus(models.Model):
    autobus = models.OneToOneField(Conductor, on_delete=models.CASCADE, primary_key=True, related_name='ultima_ubicacion')
    latitud = models.DecimalField(max_digits=10, decimal_places=8, verbose_name='Latitud')
    longitud = models.DecimalField(max_digits=11, decimal_places=8, verbose_name='Longitud')
    fecha_hora = models.DateTimeField(auto_now=True, verbose_name='Fecha y Hora')
    
    class Meta:
        verbose_name = 'Última Ubicación de Autobús'
        verbose_name_plural = 'Últimas Ubicaciones de Autobús'
        
    def __str__(self):
        return f"Ubicación de {self.autobus.nombre} {self.autobus.apellido} - {self.fecha_hora}"