from xml.sax.handler import property_declaration_handler
from django import forms
from online.models import Consultas

class FormConsultas(forms.ModelForm):
    class Meta:
        model = Consultas
        fields = '__all__'