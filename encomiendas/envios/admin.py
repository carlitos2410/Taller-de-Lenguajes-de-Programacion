from django.contrib import admin
from .models import Encomienda


@admin.register(Encomienda)
class EncomiendaAdmin(admin.ModelAdmin):
    list_display = (
        'codigo',
        'cliente',
        'ruta',
        'descripcion',
        'peso_kg',
        'estado',
        'fecha_envio',
    )
    list_filter = ('estado', 'ruta')
    search_fields = (
        'codigo',
        'descripcion',
        'cliente__nombres',
        'cliente__apellidos',
        'cliente__dni',
    )