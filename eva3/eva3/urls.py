"""eva3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from logging import logMultiprocessing
from django.contrib import admin
from django.urls import path, include
from online.views import listaConsultas, agregarConsulta, index, pagCliente, pagTecnico, loginPage, validarUsuario, salir, eliminarConsultas, actualizarConsulta
from administrador.views import panelAdministrador
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('inicio/', loginPage),
    path('salir', salir),
    path('inicio/salir', salir),
    path('accounts/', include('django.contrib.auth.urls')),
    path('inicio/listaConsultas/', listaConsultas),
    path('inicio/agregarConsulta/', agregarConsulta),
    path('inicio/paginaTecnico/', pagTecnico),
    path('inicio/paginaCliente/', pagCliente),
    path('inicio/paginaAdministrador/', panelAdministrador),
    path('eliminarConsultas/<int:id>', eliminarConsultas),
    path('actualizarConsultas/<int:id>', actualizarConsulta),
    path('Logout/', LogoutView.as_view(template_name='logout.html'), name='Logout'),
]