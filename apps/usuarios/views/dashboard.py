import re
from django.shortcuts import render, redirect
from django.contrib import auth, messages
from usuarios.models import Usuario


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
                return redirect('dashboard')

    return render(request, 'admin/login.html')


def logout(request):
    auth.logout(request)
    messages.error(
        request, 'Logout realizado com sucesso')
    return redirect('login')


def dashboard(request):
    if request.user.is_authenticated:
        usuario = request.user.id
        return render(request, 'admin/dashboard/index.html')
    else:
        return redirect('login')


def campo_vazio(campo):
    return not campo.strip()
