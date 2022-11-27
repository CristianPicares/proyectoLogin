from django.shortcuts import render
from django.shortcuts import redirect
from online.models import Consultas
from online.forms import FormConsultas
from . import forms

# Create your views here.
def loginPage(request):
    return render(request, 'loginPage.html')

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

def pagAdministrador(request):
    return render(request, 'admninistrador.html')

def ValidarUsuario(request):
    if request.user.is_authenticated:
        if request.user.groups.name  == "Cliente":
            return redirect('paginaCliente/')
        elif request.user.groups.name == "Administrador":
            return redirect('paginaAdministrador/')
        elif request.usser.groups.name == "TecnicoMaster":
            return redirect('paginaTenicoMaster/')
        elif request.user.is_admin:
            return redirect('/admin/')
    return redirect('login')

def agregarConsulta(request):
    form = forms.FormConsultas()
    if request.method == 'POST':
        form = FormConsultas(request.POST)
        if form.is_valid():
            form.save()
        return listaConsultas(request)
    data = {'form' : form}
    return render(request, 'agregarConsulta.html', data)
