from apps import usuarios
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from usuarios.models import Usuario
from usuarios.forms import UsuarioFormularioModificacao


def login(request):
    """Realiza o login do usuário no sistema de gerenciamento do CME"""
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']

        if campo_vazio(email) or campo_vazio(senha):
            messages.error(
                request, 'Os campos email e senha não podem ficar em branco')
            return redirect('login')

        elif Usuario.objects.filter(email=email).exists():
            nome = Usuario.objects.filter(email=email).values_list(
                'username', flat=True).get()
            usuario = auth.authenticate(request, username=nome, password=senha)
            if usuario is not None:
                auth.login(request, usuario)
                return redirect(reverse('dashboard', args=[usuario.id]))

    return render(request, 'admin/login.html')


def logout(request):
    auth.logout(request)
    messages.error(
        request, 'Logout realizado com sucesso')
    return redirect('login')


@login_required
def dashboard(request, id):
    usuario = get_object_or_404(Usuario, pk=id)
    dados = {
        'usuario': usuario
    }
    return render(request, 'admin/dashboard/index.html', dados)


@login_required
def perfil(request, id):
    usuario = get_object_or_404(Usuario, pk=id)
    if request.method == 'POST':
        form = UsuarioFormularioModificacao(data=request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('perfil')
    else:
        form = UsuarioFormularioModificacao(instance=usuario)
    dados = {
        'form': form,
        'usuario': usuario
    }
    return render(request, 'admin/dashboard/perfil.html', dados)


def campo_vazio(campo):
    return not campo.strip()
