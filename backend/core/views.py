from django.shortcuts import render

def index(request):

    dados = {}

    return render(request, 'core/index.html', dados)
