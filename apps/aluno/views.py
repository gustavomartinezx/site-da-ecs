
from django.shortcuts import render, get_object_or_404, redirect
from .models import Aluno
from .forms import AlunoForm
from django.urls import reverse

def aluno_list(request):
    alunos = Aluno.objects.all()
    return render(request, "alunos.html", {"alunos": alunos})

def aluno_create(request):
    if request.method == "POST":
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("aluno:aluno_list"))
    else:
        form = AlunoForm()
    return render(request, "aluno_form.html", {"form": form})

def aluno_update(request, pk):
    aluno = get_object_or_404(Aluno, pk=pk)
    if request.method == "POST":
        form = AlunoForm(request.POST, instance=aluno)
        if form.is_valid():
            form.save()
            return redirect(reverse("aluno:aluno_list"))
    else:
        form = AlunoForm(instance=aluno)
    return render(request, "aluno_update.html", {"form": form, "aluno": aluno})

def aluno_delete(request, pk):
    aluno = get_object_or_404(Aluno, pk=pk)
    if request.method == "POST":
        aluno.delete()
        return redirect(reverse("aluno:aluno_list"))
    return render(request, "aluno_confirm_delete.html", {"aluno": aluno})
