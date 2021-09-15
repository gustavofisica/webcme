from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Noticia
from configuracoes.models import Configuracoes
from usuarios.models import Usuario
from noticias.forms import FormularioNoticia

# Create your views here.
def noticia(request, slug):
    """Renderiza uma única notícia"""
    noticia = get_object_or_404(Noticia, slug=slug)
    categorias = Noticia.ESCOLHAS_CATEGORIA 
    lista_categorias = lista_de_categorias(categorias)

    dados = {
        'noticia': noticia,
        'categorias': lista_categorias,
    }

    return render(request, 'noticias/noticia.html', dados)

def lista_noticias(request, categoria):
    """Mostra uma lista de notícias classificada por categoria"""
    if categoria == 'todas':
        noticias = Noticia.objects.order_by('-edicao').all()
    else:        
        noticias = Noticia.objects.order_by('-edicao').filter(categoria=categoria)
    
    configuracoes = Configuracoes.objects.last()
    numero_de_noticias_renderizadas = configuracoes.noticias_index
    categorias = Noticia.ESCOLHAS_CATEGORIA    
    lista_categorias = lista_de_categorias(categorias)

    paginator = Paginator(noticias, numero_de_noticias_renderizadas)
    page = request.GET.get('page')
    noticias_por_pagina = paginator.get_page(page)

    dados = {
        'noticias': noticias_por_pagina,
        'categorias': lista_categorias,
    }

    return render(request, 'noticias/lista_noticias.html', dados)

def lista_de_categorias(categorias):
    """Retorna uma lista de categorias de notícias"""
    lista_categorias = []

    for categoria in categorias:
        lista_categorias.append(categoria[0])

    return lista_categorias

@login_required
def nova_noticia(request, username):

    usuario = usuario = get_object_or_404(Usuario, username=username)

    form = FormularioNoticia()

    dados = {
        'usuario': usuario,
        'form': form
    }

    return render(request, 'admin/dashboard/noticias/nova_noticia.html', dados)
