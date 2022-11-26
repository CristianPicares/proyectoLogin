from django.shortcuts import render
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

def agregarConsulta(request):
    form = forms.FormConsultas()
    if request.method == 'POST':
        form = FormConsultas(request.POST)
        if form.is_valid():
            form.save()
        return listaConsultas(request)
    data = {'form' : form}
    return render(request, 'agregarConsulta.html', data)
