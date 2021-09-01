from django.shortcuts import render, redirect, get_object_or_404
from .functions import gerar_dados_do_usuario
from django.contrib import messages
from usuarios.models import Usuario, Docente
from usuarios.forms import UsuarioFormularioCriacao
import uuid
from django.core.files.storage import FileSystemStorage


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
        if Usuario.objects.filter(email=email).exists():
            messages.error(request, 'Usuário já cadastrado')
            return redirect('cadastro')
        else:
            usuario = Usuario.objects.create_user(username=username, foto_de_perfil=foto_de_perfil, caminho_armazenamento=username, first_name=first_name, last_name=last_name, email=email, curriculo_lattes=curriculo_lattes,
                                                  celular=celular,
                                                  is_staff=False,
                                                  is_active=True, eh_conselheiro=False, eh_docente=True, eh_discente=False, eh_tecnico=False, eh_chefe=False, eh_sub_chefe=False, operacao={})
            usuario.set_password(password1)
            usuario.save()

            docente = Docente.objects.create(
                usuario=usuario, instituicional=instituicional, ramal=ramal)
            docente.save()
            messages.success(request, 'Docente cadastrado com sucesso')
            return redirect('login')


def cadastro_externos(request):
    return render(request, 'admin/cadastros/cadastro_externos.html')


def senhas_nao_sao_iguais(senha, senha2):
    return senha != senha2
