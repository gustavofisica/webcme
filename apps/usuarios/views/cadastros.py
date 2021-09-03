from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from usuarios.utils import gerar_token
from django.utils.encoding import force_bytes, force_str, force_text, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.shortcuts import render, redirect, get_object_or_404
from .functions import gerar_dados_do_usuario
from django.contrib import messages
from usuarios.models import Usuario, Docente
import uuid
from django.core.mail import EmailMessage


def cadastro(request):
    if request.method == 'POST':
        dados = gerar_dados_do_usuario(request.POST['nome'])
        if dados['tipo_de_usuario'] == 'discente':
            dados_do_discente = {
                'dados': dados
            }
            return render(request, 'admin/cadastros/cadastro_discente.html', dados_do_discente)
        elif dados['tipo_de_usuario'] == 'docente':
            dados_do_docente = {
                'dados': dados
            }
            return render(request, 'admin/cadastros/cadastro_docente.html', dados_do_docente)
        else:
            messages.error(request, 'Usuário não encontrado no SIGA')
            return redirect('cadastro')
    else:
        return render(request, 'admin/cadastros/cadastro.html')


def cadastro_docente(request):
    if request.method == 'POST':
        username = uuid.uuid4()
        if 'imagem_uploads' in request.FILES:
            foto_de_perfil = request.FILES['imagem_uploads']
        else:
            foto_de_perfil = ''
        first_name = request.POST['nome']
        last_name = request.POST['sobrenome']
        ramal = request.POST['ramal']
        celular = request.POST['celular']
        email = request.POST['email']
        curriculo_lattes = request.POST['lattes']
        departamentos = []
        for campo in request.POST:
            if 'departamento' in campo:
                departamentos.append(request.POST[campo])

        instituicional = {
            'instituição': request.POST['instituicao'],
            'setor': request.POST['setor'],
            'departamentos': departamentos
        }

        password1 = request.POST['senha']
        password2 = request.POST['confirma-senha']
        if senhas_nao_sao_iguais(password1, password2):
            messages.error(request, 'As senhas não são iguais')
            return redirect('cadastro')
        if email_valido(email):
            messages.error(request, 'O e-mail não é válido')
        if Usuario.objects.filter(email=email).exists():
            messages.error(request, 'Usuário já cadastrado')
            return redirect('cadastro')
        else:
            usuario = Usuario.objects.create_user(username=username, foto_de_perfil=foto_de_perfil, caminho_armazenamento=username, first_name=first_name, last_name=last_name, email=email, curriculo_lattes=curriculo_lattes,
                                                  celular=celular,
                                                  is_staff=False,
                                                  is_active=False, eh_conselheiro=False, eh_docente=True, eh_discente=False, eh_tecnico=False, eh_chefe=False, eh_sub_chefe=False, operacao={})
            usuario.set_password(password1)
            usuario.save()

            docente = Docente.objects.create(
                usuario=usuario, instituicional=instituicional, ramal=ramal)
            docente.save()

            email_de_ativacao(request, usuario)

            messages.success(
                request, 'Docente cadastrado com sucesso. Você precisa verificar seu e-mail para ter acesso ao Dashboard')
            return redirect('login')
    else:
        return render(request, 'admin/cadastros/cadastro_docente.html')


def cadastro_externos(request):
    return render(request, 'admin/cadastros/cadastro_externos.html')


def ativar_usuario(request, usuario_id64, token):
    try:
        usuario_id = force_text(urlsafe_base64_decode(usuario_id64))
        usuario = Usuario.objects.get(pk=usuario_id)

    except Exception as e:
        usuario = None

    if usuario and gerar_token.check_token(usuario, token):
        usuario.is_active = True
        usuario.save()
        messages.success(request, 'E-mail verificado com sucesso')
        return redirect('login')

    return render(request, 'admin/cadastros/falha_ativacao.html', {'usuario': usuario})


def senhas_nao_sao_iguais(senha, senha2):
    return senha != senha2


def email_valido(email):
    return False


def email_de_ativacao(request, usuario):
    site_corrente = get_current_site(request)
    assunto_do_email = 'Ativar sua conta no CME'
    corpo_do_email = render_to_string('admin/cadastros/ativacao.html', {
        'usuario': usuario,
        'dominio': site_corrente,
        'usuario_id': urlsafe_base64_encode(force_bytes(usuario.pk)),
        'token': gerar_token.make_token(usuario)
    })

    email = EmailMessage(subject=assunto_do_email, body=corpo_do_email,
                         from_email=settings.EMAIL_FROM_USER,
                         to=[usuario.email])
    email.send()
