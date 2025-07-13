from django import forms
from .models import Extensionista

class ExtensionistaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        base_classes = 'w-full px-3 py-2 bg-gray-900 border border-gray-600 rounded-lg text-gray-300 focus:outline-none focus:ring-2 focus:ring-green-500 focus:border-green-500 transition-colors'
        text_input_classes = f'pl-10 {base_classes}'

        self.fields['nome'].widget.attrs.update({'class': text_input_classes})
        self.fields['cpf'].widget.attrs.update({'class': text_input_classes})
        self.fields['rgm'].widget.attrs.update({'class': text_input_classes})
        self.fields['area'].widget.attrs.update({'class': base_classes})
        self.fields['status'].widget.attrs.update({
            'class': 'sr-only peer' # 'sr-only' esconde visualmente, 'peer' ativa o controle do Tailwind
        })
        if self.instance.pk is None: 
             self.initial['status'] = True 


    class Meta:
        model = Extensionista
        fields = ['nome', 'cpf', 'rgm', 'area', 'status']
