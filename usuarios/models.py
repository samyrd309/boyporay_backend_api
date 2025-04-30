from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

# Create your models here.

class UsuarioAdministrador(AbstractUser):
    rol = models.CharField(max_length=100, blank=True, null=True)
    groups = models.ManyToManyField(Group, blank=True, related_name='admin_users_group', verbose_name='groups')
    user_permissions = models.ManyToManyField(Permission, blank=True, related_name='user_permisions', verbose_name='admin_users_permissions')
    class Meta:
        verbose_name = 'Usuario Administrador'
        verbose_name_plural = 'Usuarios Administradores'
        
class Conductor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    cedula = models.CharField(max_length=8, unique=True)
    telefono = models.CharField(max_length=15, unique=True)
    direccion = models.CharField(max_length=255)
    fecha_nacimiento = models.DateField()
    email = models.EmailField(unique=True)
    
    class Meta:
        verbose_name = 'Conductor'
        verbose_name_plural = 'Conductores'
        
    def __str__(self):
        return self.usuario.username
    
class UsuarioPasajero(AbstractUser):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    cedula = models.CharField(max_length=8, unique=True)
    telefono = models.CharField(max_length=15, unique=True)
    direccion = models.CharField(max_length=255)
    fecha_nacimiento = models.DateField()
    email = models.EmailField(unique=True)
    groups = models.ManyToManyField(Group, verbose_name='groups', blank=True, related_name="pasajero_users_groups")
    user_permissions = models.ManyToManyField(Permission, verbose_name='user_permissions', blank=True, related_name="pasajero_users_permissions")
    class Meta:
        verbose_name = 'Usuario Pasajero'
        verbose_name_plural = 'Usuarios Pasajeros'
        
    def __str__(self):
        return self.usuario.username
"""  
class Favoritos(models.Model):
    usuario = models.ForeignKey(UsuarioPasajero, on_delete=models.CASCADE, related_name='favoritos', verbose_name='Usuario')
    parada = models.ForeignKey('paradas.Parada', on_delete=models.CASCADE, verbose_name='Parada')
    fecha_agregado = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Favorito'
        verbose_name_plural = 'Favoritos'
        unique_together = ('usuario', 'parada')
        
    def __str__(self):
        return f"{self.usuario.username} - {self.parada.nombre}"
"""