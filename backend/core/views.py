from django.shortcuts import render
from backend.core.models import Config

def index(request):
    #config = Config.objects.get(id=1)

    dados = {
        "titulo" : "Minha página",
        "navCor" : "#ffffff",
        "textNavCor" : "#000000",
    }

    return render(request, 'core/index.html', dados)
