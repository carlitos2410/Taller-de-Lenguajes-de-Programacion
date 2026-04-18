from django.db import models


class Ruta(models.Model):
    origen = models.CharField(max_length=100)
    destino = models.CharField(max_length=100)
    distancia_km = models.DecimalField(max_digits=8, decimal_places=2)
    tiempo_estimado = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.origen} → {self.destino}"

    class Meta:
        verbose_name = 'Ruta'
        verbose_name_plural = 'Rutas'
        ordering = ['origen', 'destino']