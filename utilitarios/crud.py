from dados.bd import *

def listar_produtos():
    dados = carregar_dados()
    return dados["produtos"]

def listar_usuarios():
    dados = carregar_dados()
    return dados["usuarios"]