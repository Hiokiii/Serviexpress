from atexit import register
from django.contrib import admin

from .models import Cliente, Cotizacion, DetalleDocumento, DetalleServicio, Documento, Empleado, GrupoProducto, MedioPago, OrdenPedidoProducto, OrdenProducto, Producto, ProvProducto, Proveedor, Reserva, Servicio, TipoDocumento, TipoEmpleado, TipoProducto, Vehiculo



# Register your models here.

admin.site.register(Cliente)
admin.site.register(Cotizacion)
admin.site.register(DetalleDocumento)
admin.site.register(DetalleServicio)
admin.site.register(Documento)
admin.site.register(Empleado)
admin.site.register(GrupoProducto)
admin.site.register(MedioPago)
admin.site.register(OrdenPedidoProducto)
admin.site.register(OrdenProducto)
admin.site.register(Producto)
admin.site.register(ProvProducto)
admin.site.register(Proveedor)
admin.site.register(Reserva)
admin.site.register(Servicio)
admin.site.register(TipoDocumento)
admin.site.register(TipoEmpleado)
admin.site.register(TipoProducto)
admin.site.register(Vehiculo)
