from django.shortcuts import render, get_object_or_404, redirect
from .models import Curso
from .forms import CursoForm
from django.urls import reverse

def curso_list(request):
    cursos = Curso.objects.all()
    return render(request, "cursos.html", {"cursos": cursos})

def curso_create(request):
    if request.method == "POST":
        post_data = request.POST.copy()
        if 'status' not in post_data:
            post_data['status'] = 'inativo'
        form = CursoForm(post_data)
        if form.is_valid():
            form.save()
            return redirect(reverse("cursos:curso_list"))
    else:
        form = CursoForm()
    return render(request, "curso_form.html", {"form": form})

def curso_update(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    if request.method == "POST":
        post_data = request.POST.copy()
        if 'status' not in post_data:
            post_data['status'] = 'inativo'
        form = CursoForm(post_data, instance=curso)
        if form.is_valid():
            curso = form.save(commit=False)
            from django.utils import timezone
            curso.atualizado_em = timezone.now()
            curso.save()
            return redirect(reverse("cursos:curso_list"))
    else:
        form = CursoForm(instance=curso)
    return render(request, "curso_update.html", {"form": form, "curso": curso})

def curso_delete(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    if request.method == "POST":
        curso.delete()
        return redirect(reverse("cursos:curso_list"))
    return render(request, "curso_confirm_delete.html", {"curso": curso})