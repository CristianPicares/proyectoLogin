from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from online.models import Consultas
from online.forms import FormConsultas
from . import forms

# Create your views here.
@login_required
def loginPage(request):
    return render(request, 'loginPage.html')

def salir(request):
    logout(request)
    return redirect('/')

def listaConsultas(request):
    consultas = Consultas.objects.all()
    data = {'consultas':consultas}
    return render(request, 'listaConsultas.html', data)

def index(request):
    return render(request,'index.html')

def pagCliente(request):
    return render(request, 'platCliente.html')

def pagTecnico(request):
    return render(request, 'platTecnico.html')

@login_required
def validarUsuario(request):
    if request.user.is_authenticated:
        if request.user.groups.name  == "Cliente":
            return redirect('paginaCliente')
        elif request.user.groups.name == "Administrador":
            return redirect('paginaAdministrador')
        elif request.user.groups.name == "TecnicoMaster":
            return redirect('paginaTenicoMaster')
    return redirect('login')

def agregarConsulta(request):
    form = forms.FormConsultas()
    if request.method == 'POST':
        form = FormConsultas(request.POST)
        if form.is_valid():
            form.save()
        return listaConsultas(request)
    data = {'form' : form,
            'titulo':'AGREGANDO PROYECTO',
             'boton':'AGREGAR PROYECTO'}

    return render(request, 'agregarConsulta.html', data)
