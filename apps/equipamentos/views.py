from django.shortcuts import render
from .models import Equipamento

# Create your views here.
def equipamentos(request):
    """Rederiza os equipamentos de microscopia"""
    equipamentos = Equipamento.objects.all()

    dados = {
        'equipamentos': equipamentos,
    }

    return render(request, 'equipamentos/equipamentos.html', dados)
