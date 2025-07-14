from django import forms
from .models import Curso

class CursoForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        base_classes = 'w-full px-3 py-2 bg-gray-900 border border-gray-600 rounded-lg text-gray-300 focus:outline-none focus:ring-2 focus:ring-green-500 focus:border-green-500 transition-colors'
        text_input_classes = f'pl-10 {base_classes}'
        select_classes = 'w-full px-3 py-2 bg-gray-900 border border-gray-600 rounded-lg text-gray-300 focus:outline-none focus:ring-2 focus:ring-green-500 focus:border-green-500 transition-colors'
        self.fields['nome'].widget.attrs.update({'class': text_input_classes})
        self.fields['status'].widget.attrs.update({'class': select_classes})

    class Meta:
        model = Curso
        fields = ['nome', 'status']
