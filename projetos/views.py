from django.shortcuts import render
from .models import Projeto
from django.contrib.auth.decorators import login_required

def index(request):
    projeto = Projeto.objects.all()
    return render(request, 'projetos/index.html', {'projetos': projeto})
    

def detalhe(request, pk):
    projeto = Projeto.objects.get(pk=pk)
    return render(request, 'projetos/detalhe.html', {'projeto': projeto})
