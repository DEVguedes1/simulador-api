from utilitarios.bd import *

def adicionar_usuario(nome, senha):
    dados = carregar_dados()
    usuarios = dados["usuarios"]

    novo_id = 1
    if usuarios:
        novo_id = max(u["id"] for u in usuarios) + 1

    novo_usuario = {
        "id": novo_id,
        "nome": nome,
        "senha": senha
    }

    usuarios.append(novo_usuario)
    salvar_dados(dados)
    print(f"Usuário '{nome}' adicionado com sucesso.")
