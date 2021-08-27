from django.shortcuts import render, redirect
from .functions import gerar_dados_do_usuario
from django.contrib import messages

# Create your views here.


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


def cadastro_externos(request):
    return render(request, 'admin/cadastros/cadastro_externos.html')
