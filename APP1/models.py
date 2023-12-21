from django.db import models
from django import forms

class cliente(models.Model):
    dni = models.CharField(max_length=8, null=False, verbose_name='DNI')
    nombre = models.CharField(max_length=20, null=False, verbose_name='Nombre')
    apellido = models.CharField(max_length=20, null=False, verbose_name='Apellido')
    tel = models.CharField(max_length=10, null=False, verbose_name='Teléfono')
    géneros = [('V', 'Varón'),('M', 'Mujer'),]
    género = models.CharField(max_length=1, choices=géneros)
    def __str__(self):
        return '%s  %s'%(self.apellido, self.nombre)  
    class Meta:
        db_table = 'cliente'
        verbose_name = 'cliente'
        verbose_name_plural = 'Clientes'

class servicio(models.Model):
    nombre = models.CharField(max_length=20, null=False, verbose_name='Nombre')
    tarifa = models.CharField(max_length=20, null=False, verbose_name='Tarifa')
    descripción = models.CharField(max_length=50, null=False, verbose_name='Descripción')
    def __str__(self):
        return '%s'%(self.nombre)  
    class Meta:
        db_table = 'servicio'
        verbose_name = 'servicio'
        verbose_name_plural = 'Servicios'
        
class tipo_habitación(models.Model):
    nombre = models.CharField(max_length=20, null=False, verbose_name='tipo')
    def __str__(self):
        return '%s'%(self.nombre)
    class Meta:
        db_table = 'tipo_habitación'
        verbose_name = 'tipoH'
        verbose_name_plural = 'Tipos de Habitaciones'

class habitación(models.Model):
    tipo = models.ForeignKey(tipo_habitación, on_delete=models.CASCADE, blank=True, null=True)
    servicios = models.ManyToManyField(servicio)
    tarifa = models.PositiveIntegerField(default=8000)
    ocupada = models.BooleanField(default=False)
    def __str__(self):
        return '%s - %s $ %s'%(self.id,self.tipo,self.tarifa)
    class Meta:
        db_table = 'habitación'
        verbose_name = 'habitación'
        verbose_name_plural = 'Habitaciones'

class reserva(models.Model):
    habitación = models.ForeignKey(habitación, on_delete=models.CASCADE, blank=True, default='1')
    cliente = models.ForeignKey(cliente, on_delete=models.CASCADE, blank=True, null=True)
    cant_días = models.PositiveIntegerField()
    def __str__(self):
        return '%s  %s'%(self.cliente,self.habitación)  
    class Meta:
        db_table = 'reserva'
        verbose_name = 'reserva'
        verbose_name_plural = 'Reservas'
        
class pago(models.Model):
    reserva = models.ForeignKey(reserva, on_delete=models.CASCADE, blank=True, null=True)
    monto = models.PositiveIntegerField()
    formas = [('C', 'Tarjeta'),('E', 'Efectivo'),('T', 'Tranferencia'),]
    forma_pago = models.CharField(max_length=1, choices=formas)
    fecha_pago = models.DateField()
    def __str__(self):
        return '%s  %s'%(self.monto,self.fecha_pago)  
    class Meta:
        db_table = 'pago'
        verbose_name = 'pago'
        verbose_name_plural = 'Pagos'