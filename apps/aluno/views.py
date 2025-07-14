
from django.shortcuts import render

def home(request):
    return render(request, "aluno_home.html")
