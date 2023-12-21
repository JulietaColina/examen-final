from django.contrib import admin
from .models import *

@admin.register(cliente)
class cliente(admin.ModelAdmin):
    list_display = ('id','dni','nombre','apellido','tel',)

@admin.register(servicio)
class servicio(admin.ModelAdmin):
    list_display = ('id','nombre','descripción','tarifa')

@admin.register(habitación)
class habitación(admin.ModelAdmin):
    list_display = ('id','tipo','tarifa',)

@admin.register(reserva)
class reserva(admin.ModelAdmin):
    list_display = ('id','cliente','habitación',)
    
@admin.register(pago)
class reserva(admin.ModelAdmin):
    list_display = ('id','reserva','monto',)

@admin.register(tipo_habitación)
class tipo_habitación(admin.ModelAdmin):
    list_display = ('id','nombre')
    
admin.site.site_header = 'Hotel Alonso'
admin.site.index_title = 'Panel de control'
admin.site.site_title = 'Administración del Hotel'