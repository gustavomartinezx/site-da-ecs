from django.shortcuts import render, redirect, get_object_or_404
from .models import Extensionista
from .forms import ExtensionistaForm

def extensionista_list(request):
    extensionistas = Extensionista.objects.all()
    return render(request, "extensionistas.html", {"extensionistas": extensionistas})

def extensionista_create(request):
    if request.method == "POST":
        form = ExtensionistaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("extensionista_list")
    else:
        form = ExtensionistaForm()
    return render(request, "extensionista_form.html", {"form": form})

def extensionista_update(request, pk):
    extensionista = get_object_or_404(Extensionista, pk=pk)
    if request.method == "POST":
        form = ExtensionistaForm(request.POST, instance=extensionista)
        if form.is_valid():
            form.save()
            return redirect("extensionista_list")
    else:
        form = ExtensionistaForm(instance=extensionista)
    return render(request, "extensionista_form.html", {"form": form})