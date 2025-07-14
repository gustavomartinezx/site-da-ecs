from django.db import models

# Create your models here.
class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    cpf = models.CharField(max_length=11, unique=True)
    responsavel = models.CharField(max_length=100, blank=True, null=True)
    telefone = models.CharField(max_length=15, blank=True, null=True)
    turma = models.ForeignKey('cursos.Curso', on_delete=models.SET_NULL, related_name='turma_alunos', blank=True, null=True)
    status = models.BooleanField(default=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.nome