from xml.sax.handler import property_declaration_handler
from django import forms
from online.models import Consultas, Respuesta

class FormConsultas(forms.ModelForm):
    class Meta:
        model = Consultas
        fields = '__all__'

class FormRespuestas(forms.ModelForm):
    class Meta:
        model = Respuesta
        fields = '__all__'