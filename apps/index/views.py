from django.shortcuts import render
from noticias.models import Noticia
from configuracoes.models import Configuracoes

# Create your views here.
def index(request):
    """Renderiza informações no index.html"""
    configuracoes = Configuracoes.objects.last()
    numero_de_noticias_renderizadas = configuracoes.noticias_index
    noticias = Noticia.objects.order_by('-criacao').filter(status=True).filter(destaque=False)[:numero_de_noticias_renderizadas]
    destaque = Noticia.objects.order_by('-criacao').filter(status=True).filter(destaque=True).first()
    
    dados = {
        'noticias': noticias,
        'destaque': destaque,
    }
    
    return render(request, 'index.html', dados)

def sistema_gerenciamento(request):
    return render(request, 'sistema_gerenciamento.html')

def normas(request):
    return render(request, 'normas.html')
