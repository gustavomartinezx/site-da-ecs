
from django.db import models

class Curso(models.Model):
    STATUS_CHOICES = [
        ("ativo", "Ativo"),
        ("inativo", "Inativo"),
    ]
    nome = models.CharField(max_length=100)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="ativo")
    instrutores = models.ManyToManyField('extensionistas.Extensionista', related_name='cursos', blank=True)
    alunos = models.ManyToManyField('aluno.Aluno', related_name='cursos', blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.nome
