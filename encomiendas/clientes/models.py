from django.db import models


class Cliente(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    dni = models.CharField(max_length=8, unique=True)
    telefono = models.CharField(max_length=15)
    direccion = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.nombres} {self.apellidos} - DNI: {self.dni}"

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['apellidos', 'nombres']