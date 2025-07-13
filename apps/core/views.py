
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from apps.extensionistas.models import Extensionista

# Create your views here.
@login_required
def home(request):
    ext_total = Extensionista.objects.count()
    ext_ativos = Extensionista.objects.filter(status=True).count()
    context = {
        'ext_total': ext_total,
        'ext_ativos': ext_ativos,
    }
    return render(request, "base.html", context)