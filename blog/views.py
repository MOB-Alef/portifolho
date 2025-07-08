from django.shortcuts import render 
from django.http import HttpResponseRedirect
from .models import Postagem , Cometario
from blog.forms import Cometarioform

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
    return render(request, 'blog/categoria.html', context)

def blog_detalhe(request, pk):
    postagem = Postagem.objects.get(pk=pk)

    form = Cometarioform()
    if request.method == 'POST':
        form = Cometarioform(request.POST)
        if form.is_valid():
            cometario = Cometario(
                autor = form.cleaned_data['nome'],
                corpo = form.cleaned_data['corpo'],
                postagem = postagem,
            )
            cometario.save()
            return HttpResponseRedirect(request.path_info)
            
    cometarios = Cometario.objects.filter(postagem=postagem)

    context = {
        'postagem': postagem,
        'comentarios': cometarios,
        'Form': Cometarioform,
    }
    return render(request, 'blog/detalhe.html', context)

