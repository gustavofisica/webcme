from bs4 import BeautifulSoup
import requests as req
import re
import datetime as dt


def acessar_siga_ufpr(identificador, operacao, metodo, url):
    """Retorna html da requisição no SIGA"""

    if metodo == 'post':

        dados_de_requisicao = {'nome': identificador, 'operacao': operacao}

        retorno_da_requisicao = req.post(url, data=dados_de_requisicao)

    elif metodo == 'get':
        url = f'https://www.prppg.ufpr.br/siga/visitante/Colaborador?idAutor={identificador}&operacao={operacao}&tipoRequisicao=ajax'

        retorno_da_requisicao = req.get(url)

    html_de_retorno = BeautifulSoup(retorno_da_requisicao.text, 'lxml')

    return html_de_retorno


def buscar_alunos_do_professor(identificador):
    """Retorna uma lista de alunos da requisição do SIGA"""

    html_de_retorno = acessar_siga_ufpr(
        identificador, 'perfilDocente', 'get', '')

    nomes_dos_docentes = html_de_retorno.find_all(
        'h3', 'profile-username text-center')

    vinculo_dos_docentes = html_de_retorno.find_all(
        'p', 'text-muted text-center')

    inicio_dos_vinculos = html_de_retorno.find_all('li', 'list-group-item')

    inicio_dos_vinculos = re.findall(r'\d+/\d+/\d+', str(inicio_dos_vinculos))

    alunos = []
    for i in range(0, len(nomes_dos_docentes), 1):
        aluno = {'nome_do_aluno': nomes_dos_docentes[i].text.strip(),
                 'nivel': vinculo_dos_docentes[i].text.strip(),
                 'inicio': dt.datetime.strptime(inicio_dos_vinculos[i], "%d/%m/%Y").strftime('%Y-%m-%d')}
        alunos.append(aluno)

    return alunos


def buscar_orientador_do_aluno(identificador):
    """Retorna o orientador principal do aluno"""

    html_de_retorno = acessar_siga_ufpr(
        identificador, 'perfilDiscente', 'get', '')

    tabela = html_de_retorno.find('table', 'table')

    tr = tabela.find_all('tr')

    td = tr[1].find_all('td')

    dados = []

    for i in range(0, len(td), 5):
        dados.append(td[i].text.strip())
        inicio = re.findall(r'\d+/\d+/\d+', str(td[i + 4].text.strip()))
        dados.append(inicio[0])

    return corrigir_espacos_tag(dados)


def corrigir_espacos_tag(lista=[]):
    """Corrige espaços e outros caracteres na lista"""

    itens_sem_espacos = []

    for item in lista:

        item = str(item).replace('\r', '')

        item = str(item).replace('\n', '')

        item = str(item).replace('\t', '')

        if item != '':

            itens_sem_espacos.append(item)

    return itens_sem_espacos


def procurar_td_na_tabela(html):
    """Procura a tag <td> no html e retorna a lista de conteúdo"""
    tabela = html.find("table", {"id": "tabela"})

    td = tabela.find_all('td')

    return td


def criar_dicionario(nome, lista, dicionario):
    """Cria um dicionário com as informações de professores ou alunos corrigidas"""
    for td in lista:

        if nome in td.text.strip() and len(nome) == len(td.text.strip()):

            for chave in dicionario:

                if chave == 'nome_do_professor' or chave == 'nome_do_aluno':
                    dicionario[chave] = lista[0].text.strip()
                elif chave == 'vinculos' or chave == 'programas':
                    item = re.findall(r'>(.*?)<', str(lista[1]), re.DOTALL)
                    dicionario[chave] = corrigir_espacos_tag(item)
                elif chave == 'alunos':
                    identificador = lista[2].find(
                        'input', {'name': 'idAutor'}).get('value')
                    dicionario[chave] = buscar_alunos_do_professor(
                        identificador)
                elif chave == 'niveis':
                    niveis = re.findall(r'>(.*?)<', str(lista[2]), re.DOTALL)
                    dicionario[chave] = corrigir_espacos_tag(niveis)
                elif chave == 'orientador' or chave == 'inicio':
                    identificador = lista[3].find(
                        'input', {'name': 'idAutor'}).get('value')
                    retorno_da_consulta_de_orientador = buscar_orientador_do_aluno(
                        identificador)
                    if chave == 'orientador':
                        dicionario[chave] = retorno_da_consulta_de_orientador[0]
                    else:
                        dicionario[chave] = retorno_da_consulta_de_orientador[1]

            return dicionario
        else:
            return f'O nome {nome} não foi encontrado no banco de dados do SIGA UFPR'.upper()


def gerar_dados_do_usuario(nome_do_usuario):
    """Retorna um dicionário com informações de professores ou alunos que estejam cadastrados no siga ou uma excessão de erro"""

    try:
        nome_do_usuario = nome_do_usuario.upper()

        texto_html_de_retorno = acessar_siga_ufpr(
            nome_do_usuario, 'buscarDocentes', 'post', 'https://www.prppg.ufpr.br/siga/visitante/ConsultarPessoa')

        if 'Nenhum docente encontrado' not in texto_html_de_retorno.text:

            td_da_tabela_de_dados = procurar_td_na_tabela(
                texto_html_de_retorno)

            dados_do_professor = criar_dicionario(nome_do_usuario, td_da_tabela_de_dados, {
                                                  'nome_do_professor': '', 'vinculos': '', 'alunos': '', 'tipo_de_usuario': ''})

            dados_do_professor['tipo_de_usuario'] = 'docente'

            return dados_do_professor
        else:

            texto_html_de_retorno = acessar_siga_ufpr(
                nome_do_usuario, 'buscarDiscentes', 'post', 'https://www.prppg.ufpr.br/siga/visitante/ConsultarDiscente')

        if 'Nenhum discente encontrado' not in texto_html_de_retorno.text:

            td_da_tabela_de_dados = procurar_td_na_tabela(
                texto_html_de_retorno)

            dados_do_aluno = criar_dicionario(nome_do_usuario, td_da_tabela_de_dados, {
                                              'nome_do_aluno': '', 'programas': '', 'niveis': '', 'orientador': '', 'inicio': '', 'tipo_de_usuario': ''})

            dados_do_aluno['tipo_de_usuario'] = 'discente'
            dados_do_aluno['inicio'] = dt.datetime.strptime(
                dados_do_aluno['inicio'], "%d/%m/%Y").strftime('%Y-%m-%d')

            return dados_do_aluno
        else:
            return {'tipo_de_usuario': 'inexistente'}
    except:
        return {'tipo_de_usuario': 'inexistente'}
