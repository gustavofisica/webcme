from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from usuarios.models import Usuario
from equipamentos.models import Equipamento, GeleriaEquipamento
from equipamentos.forms import FormularioEquipamento, FormularioGeleriaEquipamento
from django.urls import reverse


@login_required
def cria_equipamento(request, username):
    usuario = get_object_or_404(Usuario, username=username)
    equipamento = Equipamento
    galeria_equipamento = FormularioGeleriaEquipamento
    if request.method == 'POST':
        form = FormularioEquipamento(
            data=request.POST, instance=equipamento)
        if form.is_valid():
            form.save()
            return redirect(reverse('dashboard', args=[usuario.id]))
    else:
        form = FormularioEquipamento()
        form_galeria = FormularioGeleriaEquipamento()
    dados = {
        'form': form,
        'form_galeria': form_galeria,
        'usuario': usuario,
    }
    return render(request, 'admin/dashboard/equipamento.html', dados)
