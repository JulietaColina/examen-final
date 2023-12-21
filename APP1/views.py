from django.shortcuts import render, redirect
from APP1.models import habitación,servicio,cliente,reserva,tipo_habitación,pago

def index(request):
    return render(request, 'index.html')

def clientes(request):
    c = cliente.objects.all()
    lista={'clientes':c}
    return render(request, 'clientes.html',lista)

def reservas(request):
    return render(request, 'reservas.html')

#SERVICIOS---------------------------------------------------------------------

def servicios(request):
    s = servicio.objects.all()
    lista={'servicios':s}
    return render(request, 'servicios.html',lista)

def serviciosEditar(request, id):
    s = servicio.objects.get(id=id)
    dato = {'servicio':s}
    return render(request, 'editar/servicios.html', dato)

def confirmar_e_servicio(request):
    id=request.POST['id']
    nombre=request.POST['nombre']
    tarifa=request.POST['tarifa']
    descripcion=request.POST['descrip']
    s=servicio.objects.get(id=id)
    s.nombre=nombre
    s.tarifa=tarifa
    s.descripción=descripcion
    s.save()
    return redirect('/servicios')

def serviciosEliminar(request, id):
    s = servicio.objects.get(id=id)
    s.delete()
    return redirect('servicios')

def serviciosAgregar(request):
    nombre=request.POST['nombre']
    tarifa=request.POST['tarifa']
    descripcion=request.POST['descrip']
    s = servicio.objects.create(nombre=nombre,tarifa=tarifa,descripción=descripcion)
    return redirect('/servicios')

#RESERVAS---------------------------------------------------------------------

def reservas(request):
    r = reserva.objects.all()
    h = habitación.objects.all()
    c = cliente.objects.all()
    lista = {
            'reservas':r,
            'hab':h,
            'clientes':c
            }
    return render(request, 'reservas.html',lista)

def reservasEditar(request, id):
    r = reserva.objects.get(id=id)
    h = habitación.objects.all()
    c = cliente.objects.all()
    dato = {
            'reserva':r,
            'hab':h,
            'clientes':c
            }
    return render(request, 'editar/reservas.html', dato)

def cambiar_estado(habi):
    h=habitación.objects.get(id=habi)
    h.ocupada='False'
    h.save()

def confirmar_e_reserva(request):
    id_cli=request.POST['cliente']
    id=request.POST['id']
    id_hab=request.POST['hab']
    h=habitación.objects.get(id=id_hab)
    id_cli=request.POST['cliente']
    c=cliente.objects.get(id=id_cli)
    días=request.POST['días']
    r=reserva.objects.get(id=id)
    habi=r.habitación.id
    cambiar_estado(habi)
    r.habitación=h
    r.cliente=c
    r.cant_días=días
    r.save()
    h.ocupada='True'
    h.save()
    return redirect('/reservas')

def reservasEliminar(request, id):
    r = reserva.objects.get(id=id)
    id_hab=r.habitación.id
    h=habitación.objects.get(id=id_hab)
    r.delete()
    h.ocupada='False'
    h.save()
    return redirect('reservas')

def reservasAgregar(request):
    id_hab=request.POST['hab']
    h=habitación.objects.get(id=id_hab)
    id_cli=request.POST['cliente']
    c=cliente.objects.get(id=id_cli)
    días=request.POST['días']
    r = reserva.objects.create(habitación=h,cliente=c,cant_días=días)
    h.ocupada='True'
    h.save()
    return redirect('/reservas')

#HABITACIONES---------------------------------------------------------------------
def habitaciones(request):
    h = habitación.objects.all()
    tipos=tipo_habitación.objects.all()
    lista={'habitaciones':h,
            'tiposH':tipos,   
        }
    return render(request, 'habitaciones.html',lista)