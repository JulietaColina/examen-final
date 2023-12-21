from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('reservas/',views.reservas,name='reservas'),
    path('habitaciones/',views.habitaciones,name='habitaciones'),
    path('servicios/',views.servicios,name='servicios'),
    path('clientes/',views.clientes,name='clientes'),
    
    path('servicios/editar_servicio/<int:id>',views.serviciosEditar),
    path('servicios/confirmar_e_servicio/',views.confirmar_e_servicio, name='edicionS'),
    path('servicios/eliminar_servicio/<int:id>',views.serviciosEliminar),
    path('servicios/registrar_servicio/',views.serviciosAgregar),

    path('reservas/editar_reserva/<int:id>',views.reservasEditar),
    path('reservas/confirmar_e_reserva/',views.confirmar_e_reserva, name='edicionR'),
    path('reservas/eliminar_reserva/<int:id>',views.reservasEliminar),
    path('reservas/registrar_reserva/',views.reservasAgregar, name='nueva_reserva'),

]