from django.shortcuts import render
from clientes.models import Cliente
from rutas.models import Ruta
from .models import Empleado, Encomienda, HistorialEstado


def dashboard(request):
    context = {
        'total_clientes': Cliente.objects.count(),
        'total_rutas': Ruta.objects.count(),
        'total_empleados': Empleado.objects.count(),
        'total_encomiendas': Encomienda.objects.count(),
        'total_historial': HistorialEstado.objects.count(),
        'encomiendas': Encomienda.objects.all()[:10],
    }
    return render(request, 'dashboard.html', context)