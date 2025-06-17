from dados.bd import *
from dados.produtos import *

def cadastro_de_produtos():
    dados = carregar_dados()
    nome = input("digite o nome do produto: ")
    
    try:
        preco=float(input("preço: "))
        
    except ValueError:
        print("formato invalido")

    cadastro_produto(nome=nome,valor=preco)
    salvar_dados(dados)
    print("Produto cadastrado!")

def listar_produtos():
    dados = carregar_dados()
    return dados["produtos"]

def listar_usuarios():
    dados = carregar_dados()
    return dados["usuarios"]

def atualizar_produto(id):
    dados = carregar_dados()

    if id not in dados["produtos"]:
        print("Produto não encontrado!")
        return
    
    print(f"Editando {dados['id']['nome']}")
    novo_nome = input(f"Novo nome (atual: {dados['id']['nome']}): ")
    novo_preco = input(f"Novo preço (atual: {dados['id']['preco']}): ")
    
    if novo_nome:
        dados['id']['nome'] = novo_nome
    if novo_preco:
        dados['id']['preco'] = float(novo_preco)
        
    salvar_dados(dados)
    print("Produto atualizado!")

def alualizar_senha(id):
    dados = carregar_dados()

    if id not in dados["usuarios"]:
        print("Usuario não encontrado!")
        return
    
    print(f"Editando {dados['id']['nome']}")
    novo_senha = input(f"Nova senha (atual: {dados['id']['senha']}): ")

    if novo_senha:
        dados['id']['senha'] =(novo_senha)
        
    salvar_dados(dados)
    print("Produto atualizado!")

def apagar_produto(id):
    dados= carregar_dados()
    dados["produtos"]=[p for p in dados["produtos"] if p["id"] != id]
    salvar_dados(dados)
    
def buscar_produto():
    dados = carregar_dados()
    id = int(input("Digite o id para buscar: "))
    for produto in dados['produtos']:
        if dados['produtos']['id'] == id:
            print(f"Nome: {dados['produtos']['nome']}\nValor: {dados['produtos']['valor']}")
            return
    print("Usuário não encontrado.")