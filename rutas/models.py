from django.db import models

# Create your models here.

class Ruta(models.Model):
    nombre = models.CharField(max_length=100, unique=True, verbose_name='Nombre de la Ruta')
    descripcion = models.TextField(blank=True, null=True, verbose_name='Descripción de la Ruta')
    origen = models.CharField(max_length=100)
    destino = models.CharField(max_length=100)
    distancia = models.DecimalField(max_digits=10, decimal_places=2)
    codigo = models.CharField(max_length=50, unique=True, verbose_name='Código de la Ruta')
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    fecha_actualizacion = models.DateTimeField(auto_now=True, verbose_name='Fecha de Actualización')
    
    class Meta:
        verbose_name = 'Ruta'
        verbose_name_plural = 'Rutas'
        
    def __str__(self):
        return self.nombre
    
class RutaParada(models.Model):
    ruta = models.ForeignKey(Ruta, on_delete=models.CASCADE, related_name='rutas_paradas')
    parada = models.ForeignKey('paradas.Paradas', on_delete=models.CASCADE, related_name='paradas_rutas')
    orden = models.PositiveIntegerField(verbose_name='Orden de la Parada')
    
    class Meta:
        verbose_name = 'Ruta-Parada'
        verbose_name_plural = 'Rutas-Paradas'
        unique_together = ('ruta', 'orden')
        ordering = ['orden']
        
    def __str__(self):
        return f"{self.ruta.nombre} - {self.parada.nombre}"