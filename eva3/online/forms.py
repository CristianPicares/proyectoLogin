from xml.sax.handler import property_declaration_handler
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from online.models import Consultas, Respuesta

class FormConsultas(forms.ModelForm):
    class Meta:
        model = Consultas
        fields = '__all__'

class FormRespuestas(forms.ModelForm):
    class Meta:
        model = Respuesta
        fields = '__all__'
        
class FormularioLogin(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(FormularioLogin, self).__init__(*args,**kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Nombre de Usuario'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'Contraseña'