from .functions import gerar_dados_do_usuario
from datetime import timedelta, datetime
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.utils.encoding import force_bytes, force_str, force_text, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.contrib import messages
from usuarios.forms import UsuarioFormularioCriacao
from usuarios.models import Usuario, Docente, Discente, Externo
from usuarios.utils import gerar_token
from usuarios.validation import *
import uuid
import threading


class EmailThread(threading.Thread):
    """Controle de Thread dos emails enviados"""

    def __init__(self, email):

        self.email = email

        threading.Thread.__init__(self)

    def run(self):

        self.email.send()

# Funções de Cadastro no Sistema de Gerenciamento do CME


def cadastro(request):
    """Entrada de cadastro com consulta no SIGA UFPR para identificar usuários internos"""

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

            messages.error(
                request, 'Nossa consulta não encontrou o usuário no cadastro do SIGA. Pode haver algum erro de digitação. Nesse caso, tente novamente ou verifique suas informações no SIGA UFPR. Você ainda pode tentar as soluções abaixo:')

            return redirect('cadastro')

    else:

        return render(request, 'admin/cadastros/cadastro.html')


def cadastro_docente(request, consultado_no_SIGA):
    """Realiza o cadastro de usuário docente."""

    consultado_no_SIGA = bool(consultado_no_SIGA)

    if request.method == 'POST':

        aceite_de_normas = request.POST.get('aceite-nomas', "")

        if not aceite_de_normas:

            messages.error(request, 'Você deve aceitar as normas')

            return redirect('cadastro')

        else:

            ramal = request.POST['ramal']

            departamentos = []

            for campo in request.POST:

                if 'departamento' in campo and 'discente' not in campo:

                    departamentos.append(request.POST[campo])

            instituicional = {
                'instituição': request.POST['instituicao'],
                'setor': request.POST['setor'],
                'departamentos': departamentos
            }

            formulario_usuario = UsuarioFormularioCriacao(request.POST)

            if formulario_usuario.is_valid():

                usuario_docente = cadastrar_usuario(
                    request, eh_docente=True, eh_discente=False, eh_externo=False)

                if isinstance(usuario_docente, Usuario):

                    docente = Docente.objects.create(
                        usuario=usuario_docente, instituicional=instituicional, ramal=ramal)

                    docente.save()

                    lista_de_discentes = cadastrar_lista_de_discentes(
                        request, docente)

                    if consultado_no_SIGA:

                        messages.success(
                            request, 'Docente cadastrado com sucesso. Por favor, verifique seu e-mail para ativação')

                        enviar_email_de_ativacao(request, usuario_docente)

                        for usuario_discente in lista_de_discentes:
                            enviar_email_de_ativacao(request, usuario_discente)

                    else:

                        messages.success(
                            request, 'Docente cadastrado com sucesso. Porém, você não foi especificado no SIGA. Entre em contato com a equipe do CME para ativar o seu cadastro')

                    return redirect('login')

            else:

                return render(request, 'admin/cadastros/cadastro.html', {'form': formulario_usuario})

    else:

        return render(request, 'admin/cadastros/cadastro_docente.html')


def cadastro_discente(request, consultado_no_SIGA):
    """Realiza cadastro de discente."""

    consultado_no_SIGA = bool(consultado_no_SIGA)

    if request.method == 'POST':

        aceite_de_normas = request.POST.get('aceite-nomas', "")

        if not aceite_de_normas:

            messages.error(request, 'Você deve aceitar as normas')

            return redirect('cadastro')

        else:

            if not Usuario.objects.filter(email=request.POST['email_docente']).exists():
                messages.error(
                    request, 'O docente orientador não consta no banco de dados, por favor solicite que o mesmo faça o cadastramento antes de realizar o seu.')
                return redirect('cadastro')

            else:

                formulario_usuario = UsuarioFormularioCriacao(request.POST)

                vinculo = request.POST['vinculo']

                inicio_vinculo = request.POST['inicio_discente']

                setor = request.POST['setor_discente']

                departamento = request.POST['departamento']

                periodo_de_permanencia = calcular_periodo_de_permanencia(
                    vinculo, inicio_vinculo)

                docente = Docente.objects.filter(
                    usuario__email=request.POST['email_docente']).get()

                if not conferir_departamento_de_docente_e_discente(docente, departamento):

                    messages.error(
                        request, 'O seu departamento não consta no registro do seu Orientador')

                    return redirect('cadastro')

                if formulario_usuario.is_valid():

                    usuario_discente = cadastrar_usuario(
                        request, eh_docente=False, eh_discente=True, eh_externo=False)

                    if isinstance(usuario_discente, Usuario):

                        discente = Discente.objects.create(
                            usuario=usuario_discente,
                            docente=docente,
                            vinculo=vinculo,
                            inicio_vinculo=inicio_vinculo,
                            setor=setor,
                            departamento=departamento,
                            periodo_de_permanencia=periodo_de_permanencia
                        )

                        discente.save()

                        if consultado_no_SIGA:

                            messages.success(
                                request, 'Discente cadastrado com sucesso. Por favor, verifique seu e-mail para ativação')

                            enviar_email_de_ativacao(request, usuario_discente)

                        else:

                            messages.success(
                                request, 'Discente cadastrado com sucesso. Porém, você não foi especificado no SIGA. Entre em contato com a equipe do CME para ativar o seu cadastro')

                        return redirect('login')
                else:

                    return render(request, 'admin/cadastros/cadastro.html', {'form': formulario_usuario})
    else:

        return render(request, 'admin/cadastros/cadastro_discente.html')


def cadastro_externos(request):
    """Realiza cadastro de usuários externos"""

    if request.method == 'POST':

        aceite_de_normas = request.POST.get('aceite-nomas', "")

        if not aceite_de_normas:

            messages.error(request, 'Você deve aceitar as normas')

            return redirect('cadastro')

        else:

            formulario_usuario = UsuarioFormularioCriacao(request.POST)

            tipo_de_instituicao = request.POST['tipo-instituicao']
            razao_social = request.POST['razao']
            cnpj = request.POST['cnpj']
            cep = request.POST['cep']
            rua = request.POST['rua']
            bairro = request.POST['bairro']
            cidade = request.POST['cidade']
            numero = request.POST['numero']
            complemento = request.POST['complemento']
            uf = request.POST['uf']
            telefone_instituicao = request.POST['telefone']

            if formulario_usuario.is_valid():

                usuario_externo = cadastrar_usuario(
                    request, eh_docente=False, eh_discente=False, eh_externo=True)

                if isinstance(usuario_externo, Usuario):

                    externo = Externo.objects.create(
                        usuario=usuario_externo,
                        tipo_de_instituicao=tipo_de_instituicao,
                        razao_social=razao_social,
                        cnpj=cnpj,
                        cep=cep,
                        rua=rua,
                        bairro=bairro,
                        cidade=cidade,
                        numero=numero,
                        complemento=complemento,
                        uf=uf,
                        telefone_instituicao=telefone_instituicao
                    )

                    externo.save()

                    messages.success(
                                request, 'Usuário cadastrado com sucesso. Por favor, verifique seu e-mail para ativação')

                    enviar_email_de_ativacao(request, usuario_externo)

                    return redirect('login')

            else:

                return render(request, 'admin/cadastros/cadastro.html', {'form': formulario_usuario})

    return render(request, 'admin/cadastros/cadastro_externos.html')

# Funções Auxiliares


def cadastrar_usuario(request, eh_docente, eh_discente, eh_externo):
    """Salva as informações de usuário no banco de dados e retorna o objeto Usuario."""

    # Informações passadas no formulário
    username = str(uuid.uuid4())

    if 'imagem_uploads' in request.FILES:

        foto_de_perfil = request.FILES['imagem_uploads']

    else:

        foto_de_perfil = ''

    first_name = request.POST['nome']
    last_name = request.POST['sobrenome']
    celular = request.POST['celular']
    email = request.POST['email1']
    curriculo_lattes = request.POST['lattes']
    password = request.POST['password1']

    usuario = Usuario.objects.create_user(
        username=username,
        foto_de_perfil=foto_de_perfil,
        caminho_armazenamento=username,
        first_name=first_name,
        last_name=last_name,
        email=email,
        curriculo_lattes=curriculo_lattes,
        celular=celular,
        is_staff=False,
        is_active=False,
        eh_conselheiro=False,
        eh_docente=eh_docente,
        eh_discente=eh_discente,
        eh_tecnico=False,
        eh_chefe=False,
        eh_sub_chefe=False,
        eh_externo=eh_externo,
        operacao={}
    )

    usuario.set_password(password)

    usuario.save()

    return usuario


def cadastrar_lista_de_discentes(request, docente):
    """Realiza o cadastro de uma lista de discentes passados no formulário de cadastro do docente, com a mesma senha do docente. 
    Retorna uma lista de discentes cadastrados, se eles já não constarem no banco de dados."""

    lista_de_discentes = []

    for campo in request.POST:

        if 'discente' in campo:

            username = str(uuid.uuid4())

            if 'nome' in campo:

                first_name = request.POST[campo]

            elif 'email' in campo:

                email = request.POST[campo]

            elif 'vinculo' in campo:

                vinculo = request.POST[campo]

            elif 'inicio' in campo:

                inicio_vinculo = request.POST[campo]

            elif 'setor' in campo:

                setor = request.POST[campo]

            elif 'departamento' in campo:

                departamento = request.POST[campo]

                if not Usuario.objects.filter(email=email).exists():

                    usuario_discente = Usuario.objects.create_user(
                        username=username,
                        caminho_armazenamento=username,
                        first_name=first_name, email=email,
                        is_staff=False,
                        is_active=False,
                        eh_conselheiro=False,
                        eh_docente=False,
                        eh_discente=True,
                        eh_tecnico=False,
                        eh_chefe=False,
                        eh_sub_chefe=False,
                        operacao={}
                    )

                    usuario_discente.set_password(
                        request.POST['password1']
                    )

                    usuario_discente.save()

                    lista_de_discentes.append(usuario_discente)

                    periodo_de_permanencia = calcular_periodo_de_permanencia(
                        vinculo, inicio_vinculo)

                    discente = Discente.objects.create(
                        usuario=usuario_discente,
                        docente=docente,
                        vinculo=vinculo,
                        inicio_vinculo=inicio_vinculo,
                        setor=setor,
                        departamento=departamento,
                        periodo_de_permanencia=periodo_de_permanencia
                    )

                    discente.save()

    return lista_de_discentes


def calcular_periodo_de_permanencia(vinculo, inicio_vinculo):
    """Calcula o tempo de parmanência do discente de acordo com o seu vínculo."""

    if vinculo == 'Iniciação Científica':

        periodo_de_permanencia = datetime.strptime(
            inicio_vinculo, "%Y-%m-%d") + timedelta(days=365)

    elif vinculo == 'Mestrado' or vinculo == 'Pós-Doutorado':

        periodo_de_permanencia = datetime.strptime(
            inicio_vinculo, "%Y-%m-%d") + timedelta(days=(365 * 2))

    elif vinculo == 'Doutorado':

        periodo_de_permanencia = datetime.strptime(
            inicio_vinculo, "%Y-%m-%d") + timedelta(days=(365 * 4))

    return periodo_de_permanencia


def conferir_departamento_de_docente_e_discente(docente, departamento_discente):
    """Relaciona os departamentos do docente com o departamento que o discente registrou. 
    Retorna verdadeiro se o departamento do discente consta no registro de departamentos do docente."""

    match = False

    for departamento in docente.instituicional['departamentos']:

        if departamento.upper().strip() == departamento_discente.upper().strip():

            match = True

    return match


def enviar_email_de_ativacao(request, usuario):
    """Envia um e-mail para ativação de cadastro do usuário."""

    site_corrente = get_current_site(request)

    assunto_do_email = 'Ativar sua conta no CME'

    corpo_do_email = render_to_string('admin/cadastros/ativacao.html', {
        'usuario': usuario,
        'dominio': site_corrente,
        'usuario_id': urlsafe_base64_encode(force_bytes(usuario.pk)),
        'token': gerar_token.make_token(usuario)
    })

    email = EmailMessage(
        subject=assunto_do_email,
        body=corpo_do_email,
        from_email=settings.EMAIL_FROM_USER,
        to=[usuario.email]
    )

    EmailThread(email).start()


def ativar_usuario(request, usuario_id64, token):
    """Ativa o usuário através do link enviado por e-mail."""

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
