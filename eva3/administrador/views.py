from django.shortcuts import render
from administrador.models import TecnicoMaster, Usuario

# Create your views here.
def panelAdministrador(request):
    return render(request, 'panelPrincipal.html')

def panelListaTecnicos(request):
    tecnicoMaster = TecnicoMaster.objects.all()
    data = {'tecnicos':tecnicoMaster}
    return render(request, 'tecnicoMaster.html', data)

def panelUsuarios(request):
    usuarios = Usuario.objects.all()
    data = {'usuarios':usuarios}
    return render(request, 'clientes.html', data)