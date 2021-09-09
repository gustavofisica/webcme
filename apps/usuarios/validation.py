def conferir_igualdade_e_nulidade_do_campo(campo1, campo2, nome_do_campo, tipo_de_campo, lista_de_erros):
    if campo1 and campo2 and campo1 != campo2:
        lista_de_erros[nome_do_campo] = f'O campo {tipo_de_campo} não encontrou correspondência'

