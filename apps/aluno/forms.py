from django import forms
from .models import Aluno

class AlunoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        from apps.cursos.models import Curso
        self.fields['turma'].queryset = Curso.objects.filter(status='ativo')

    class Meta:
        model = Aluno
        fields = ['nome', 'email', 'cpf', 'responsavel', 'telefone', 'turma', 'status']
