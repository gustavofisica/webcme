from django.shortcuts import render

# Create your views here.
def cadastro(request):
    return render(request, 'admin/cadastros/cadastro.html')

def cadastro_externos(request):
    return render(request, 'admin/cadastros/cadastro_externos.html')
