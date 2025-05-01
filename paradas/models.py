from django.db import models

# Create your models here.

class Paradas(models.Model):
    nombre = models.CharField(max_length=255, unique=True, verbose_name='Nombre de la Parada')
    latitud = models.DecimalField(max_digits=9, decimal_places=6, verbose_name='Latitud')
    longitud = models.DecimalField(max_digits=9, decimal_places=6, verbose_name='Longitud')
    codigo = models.CharField(max_length=50, unique=True, verbose_name='Código de la Parada')
    descripcion = models.TextField(blank=True, null=True, verbose_name='Descripción de la Parada')
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    fecha_actualizacion = models.DateTimeField(auto_now=True, verbose_name='Fecha de Actualización')
    
    class Meta:
        verbose_name = 'Parada'
        verbose_name_plural = 'Paradas'
        unique_together = ('latitud', 'longitud')  # Asegura que no haya paradas con la misma latitud y longitud
        
    def __str__(self):
        return self.nombre