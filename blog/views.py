from django.shortcuts import render 
from .models import Projeto, Postagem

def blog_index(request):
    postagens= Postagem.objects.all()

    context = {
        'postagem': postagens,
    }
    postagens = Postagem.objects.all()
    return render(request, 'blog/index.html', context)

def blog_detalhe(categoria, request):
    Postagens = Postagem.objects.filter(
        categorias_name_contains=categoria 
    ).order_by('-criado_em')

    context = {
        'postagens': Postagens,
        'categorias': categoria,
    }
    return render(request, 'blog/detalhe.html', context)