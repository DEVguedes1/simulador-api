import re
from dados.bd import *
from dados.produtos import *
from dados.usuarios import *

def validar_senha(senha):
    padrao = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
    return bool(re.match(padrao, senha))

def cadastrar_usuario():
    dados = carregar_dados()
    nome = input("Nome: ")

    senha = input("Senha: ")
    if not validar_senha(senha):
        print("Senha inválida!")
        return

    adicionar_usuario(nome,senha)

    salvar_dados(dados)
    print("Usuário cadastrado com sucesso!")
