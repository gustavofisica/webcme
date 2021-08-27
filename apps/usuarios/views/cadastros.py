from django.shortcuts import render

# Create your views here.
def cadastro(request):
    return render(request, 'admin/cadastros/cadastro.html')

def cadastro_externos(request):
    return render(request, 'admin/cadastros/cadastro_externos.html')

from bs4 import BeautifulSoup
import requests as req
import re

def verificaNomeNoSiga(nome):
    url = 'https://www.prppg.ufpr.br/siga/visitante/ConsultarPessoa'

    nome = nome.upper()

    payload = {'nome': nome, 'operacao': 'buscarDocentes'}

    site = req.post(url, data=payload)

    soup = BeautifulSoup(site.text, 'lxml')

    tabela = soup.find("table", {"id": "tabela"})

    td = tabela.find_all('td')

    input = tabela.find('input', {'name': 'idAutor'}).get('value')

    url_alunos = f'https://www.prppg.ufpr.br/siga/visitante/Colaborador?idAutor={input}&operacao=perfilDocente&tipoRequisicao=ajax'

    site_alunos = req.get(url_alunos)

    soup_alunos = BeautifulSoup(site_alunos.text, 'lxml')

    alunos = soup_alunos.find_all("h3", {"class": "profile-username"})

    tipos = soup_alunos.find_all("p", {"class": "text-muted text-center"})

    inicios = soup_alunos.find_all("a", {"class": "pull-right"})

    aluno = []
    tipo = []
    for tag in alunos:
        aluno.append((tag.text.strip()).upper())
    for tag in tipos:
        tipo.append((tag.text.strip()).upper())

    inicio = re.findall(r'\d{2}/\d{2}/\d{4}', str(inicios))

    lista_alunos = []
    for i in range(len(aluno)):
        individuo = (aluno[i], tipo[i], inicio[i])
        lista_alunos.append(individuo)

    for tag in td:
        if nome in tag:
            pessoa = td[0].text.strip()
            vinculos = re.findall(r'>(.*?)<', str(td[1]).upper())
            break

    lista = {'nome': pessoa,
             'vinculos': vinculos,
             'alunos': lista_alunos}

    print(lista)
