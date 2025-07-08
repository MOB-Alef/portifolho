from django.shortcuts import render, get_object_or_404
from .models import Projeto

def index(request):
    projetos = Projeto.objects.filter(publicado=True)
    return render(request, 'projetos/index.html', {'projetos': projetos})

def detalhe(request, pk):
    projeto = get_object_or_404(Projeto, pk=pk)
    return render(request, 'projetos/detalhe.html', {'projeto': projeto})


