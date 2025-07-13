from django import forms
from .models import Extensionista

class ExtensionistaForm(forms.ModelForm):
    class Meta:
        model = Extensionista
        fields = ['nome', 'cpf', 'rgm', 'area']
