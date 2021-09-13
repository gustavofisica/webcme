from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from noticias.models import Noticia
from configuracoes.models import Configuracoes
from django.core.mail import EmailMessage
from django.conf import settings

# Create your views here.


def index(request):
    """Renderiza informações no index.html"""

    configuracoes = Configuracoes.objects.last()

    numero_de_noticias_renderizadas = configuracoes.noticias_index

    noticias = Noticia.objects.order_by(
        '-criacao').filter(status=True).filter(destaque=False)[:numero_de_noticias_renderizadas]

    destaque = Noticia.objects.order_by(
        '-criacao').filter(status=True).filter(destaque=True).first()

    dados = {
        'noticias': noticias,
        'destaque': destaque,
    }

    return render(request, 'index.html', dados)


def normas(request):
    """Renderiza a página de normas para os serviços do CME"""
    return render(request, 'normas.html')

def contato(request):
    """Envia e-mail de contato do formulário da Index"""

    assunto_do_email = f'Contato de {request.POST["nome"]}'

    corpo_do_email = render_to_string('emails/contato.html', {
        'remetente': request.POST['nome'],
        'email': request.POST['email'],
        'mensagem': request.POST['mensagem']
    })

    email = EmailMessage(
        subject=assunto_do_email,
        body=corpo_do_email,
        from_email=request.POST['email'],
        to=[settings.EMAIL_FROM_USER, request.POST['email']]
    )

    email.send()

    return redirect('index')

