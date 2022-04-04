from django.shortcuts import render
from backend.core.models import Config

def index(request):
    config = Config.objects.get(id=1)

    dados = {
        "titulo" : config.tituloPag,
        "navCor" : config.navBarCor,
        "textNavCor" : config.textNavBarCor,
    }

    return render(request, 'core/index.html', dados)
