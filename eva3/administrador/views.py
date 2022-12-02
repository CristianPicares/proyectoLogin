from django.shortcuts import render
from administrador.models import TecnicoMaster, Usuario
from django.contrib.auth import get_user_model


# Create your views here.
def panelAdministrador(request):
    user = get_user_model()
    data = user.objects.all()
    return render(request, 'administrador.html', data)

def panelListaTecnicos(request):
    tecnicoMaster = TecnicoMaster.objects.all()
    data = {'tecnicos':tecnicoMaster}
    return render(request, 'tecnicoMaster.html', data)

def panelUsuarios(request):
    usuarios = Usuario.objects.all()
    data = {'usuarios':usuarios}
    return render(request, 'clientes.html', data)
