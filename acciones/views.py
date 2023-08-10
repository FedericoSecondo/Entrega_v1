from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import Accion, CompraAccion, ResultadoEconomico, CEOEmpresa
from .forms import AgregarAccionForm
from .forms import CEOEmpresaForm
from .forms import ResultadoEconomicoForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404






# Create your views here.
def index(request):
    return render(request,"acciones/base.html")

""" def lista_acciones(request):
   acciones = Accion.objects.all()
   return render(request, 'acciones/lista_acciones.html', {'acciones': acciones}) """

def lista_compras(request):
    compras = CompraAccion.objects.all()
    return render(request, 'acciones/lista_compras.html', {'compras': compras})

def lista_resultados_economicos(request):
    resultados = ResultadoEconomico.objects.all()
    return render(request, 'acciones/lista_resultados_economicos.html', {'resultados': resultados})

def lista_ceos(request):
    ceos = CEOEmpresa.objects.all()
    return render(request, 'acciones/lista_ceos.html', {'ceos': ceos})

#----------------------------------------------------------------
#FORMULARIOS:
#----------------------------------------------------------------

#Esta seccion Contiene los Funciones para Crear


# Con esta Funcion Puedo Crear una nueva accion a monitorear
def agregar_accion(request):
    if request.method == 'POST':
        form = AgregarAccionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_acciones')  
    else:
        form = AgregarAccionForm()

    return render(request, 'acciones/agregar_accion.html', {'form': form})


# Con esta Funcion Puedo Crear una nueva informacion financiera de las empresas

def agregar_ceo(request):
    if request.method == 'POST':
        form = CEOEmpresaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_ceos')  
    else:
        form = CEOEmpresaForm()
    return render(request, 'acciones/agregar_ceo.html', {'form': form})

# Con esta Funcion Puedo Crear una nueva informacion sobre resultados economicos

def agregar_resultado(request):
    if request.method == 'POST':
        form = ResultadoEconomicoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_resultados')
    else:
        form = ResultadoEconomicoForm()
    
    return render(request, 'acciones/agregar_resultado.html', {'form': form})

#Falta una funcion para crear nuevas acciones compradas (Hay algun tema con el usuario, y eso me esta dificultando la creacion, revisar)

#------------------------------------------------------------------------------
#CRUDS
#------------------------------------------------------------------------------


#Con esta Funcion puedo realizar Updates (Editar) las acciones a monitorear

def lista_acciones(request):
    ctx={"acciones":Accion.objects.all()}
    return render(request,"acciones/lista_acciones.html",ctx)


def updateAccion(request, id_accion):
    accion = Accion.objects.get(id=id_accion)

    if request.method == "POST":
        miForm = AgregarAccionForm(request.POST, instance=accion)
        if miForm.is_valid():
            miForm.save()
            return redirect(reverse_lazy("lista_acciones"))
    else:
        miForm = AgregarAccionForm(instance=accion)

    return render(request, "acciones/agregar_accion.html", {"form": miForm})

#Con esta Funcion puedo realizar Delete (Borrar) las acciones a monitorear

def deleteAccion(request, id_accion):
    accion = get_object_or_404(Accion, id=id_accion)
    
    if request.method == "POST":
        accion.delete()
        return redirect(reverse_lazy("lista_acciones"))
    
    return render(request, "acciones/delete_accion.html", {"accion": accion})

#Con esta Funcion puedo realizar Updates (Editar) la informacion financiera de empresas

def editar_ceo(request, ceo_id):
    try:
        ceo = CEOEmpresa.objects.get(id=ceo_id)
    except CEOEmpresa.DoesNotExist:
        return redirect('lista_ceos')

    if request.method == 'POST':
        form = CEOEmpresaForm(request.POST, instance=ceo)
        if form.is_valid():
            form.save()
            return redirect('lista_ceos')
    else:
        form = CEOEmpresaForm(instance=ceo)

    return render(request, 'acciones/agregar_ceo.html', {'form': form})


#Con esta Funcion puedo realizar Deletes (Borrar) la informacion financiera de empresas

def eliminar_ceo(request, id_ceo):
    ceo = CEOEmpresa.objects.get(pk=id_ceo)
    
    if request.method == 'POST':
        ceo.delete()
        return redirect('lista_ceos')
    
    return render(request, 'acciones/eliminar_ceo.html', {'ceo': ceo})




