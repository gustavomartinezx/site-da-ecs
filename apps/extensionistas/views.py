from django.shortcuts import render, redirect, get_object_or_404
from .models import Extensionista
from .forms import ExtensionistaForm


def extensionista_delete(request, pk):
    extensionista = get_object_or_404(Extensionista, pk=pk)
    if request.method == "POST":
        extensionista.delete()
        return redirect("extensionistas:extensionista_list")
    return render(request, "extensionista_confirm_delete.html", {"extensionista": extensionista})

def extensionista_list(request):
    extensionistas = Extensionista.objects.all()
    semestres = set()
    for ext in extensionistas:
        year = ext.created_at.year
        month = ext.created_at.month
        semestre = f"{year}.1" if month <= 6 else f"{year}.2"
        semestres.add(semestre)
    semestres = sorted(semestres, reverse=True)
    return render(request, "extensionistas.html", {"extensionistas": extensionistas, "semestres": semestres})

def extensionista_create(request):
    if request.method == "POST":
        form = ExtensionistaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("extensionistas:extensionista_list")
    else:
        form = ExtensionistaForm()
    return render(request, "extensionista_form.html", {"form": form})

def extensionista_update(request, pk):
    extensionista = get_object_or_404(Extensionista, pk=pk)
    if request.method == "POST":
        form = ExtensionistaForm(request.POST, instance=extensionista)
        if form.is_valid():
            form.save()
            return redirect("extensionistas:extensionista_list")
    else:
        form = ExtensionistaForm(instance=extensionista)
    return render(request, "extensionista_update.html", {"form": form})