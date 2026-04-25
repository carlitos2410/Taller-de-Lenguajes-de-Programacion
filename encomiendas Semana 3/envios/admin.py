from django.contrib import admin
from .models import Empleado, Encomienda, HistorialEstado


class HistorialEstadoInline(admin.TabularInline):
    model = HistorialEstado
    extra = 0
    readonly_fields = (
        'estado_anterior',
        'estado_nuevo',
        'empleado',
        'fecha_cambio',
        'observacion',
    )
    can_delete = False


@admin.register(Encomienda)
class EncomiendaAdmin(admin.ModelAdmin):
    list_display = (
        'codigo',
        'remitente',
        'destinatario',
        'ruta',
        'estado',
        'costo_envio',
        'fecha_registro',
    )
    list_filter = ('estado', 'ruta')
    search_fields = (
        'codigo',
        'remitente__nro_doc',
        'destinatario__nro_doc',
        'descripcion',
    )
    readonly_fields = ('fecha_registro',)
    inlines = [HistorialEstadoInline]


@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'apellidos', 'nombres', 'cargo', 'estado')
    search_fields = ('codigo', 'apellidos', 'nombres')
    list_filter = ('estado', 'cargo')


@admin.register(HistorialEstado)
class HistorialEstadoAdmin(admin.ModelAdmin):
    list_display = (
        'encomienda',
        'estado_anterior',
        'estado_nuevo',
        'empleado',
        'fecha_cambio',
    )
    readonly_fields = ('fecha_cambio',)