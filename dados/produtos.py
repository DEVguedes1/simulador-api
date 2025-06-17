from bd import *

contador_id = 0
def cadastro_produto(produtos,nome,valor):
    dados = carregar_dados()
    produtos = dados["produtos"]
    
    if id in produtos:
            print("Produto já existe!")
            return
    else:
        global contador_id
        contador_id += 1
        produtos.append({"id": contador_id, "nome":nome,"preco":valor})
        
        salvar_dados(dados)
        print(f"Produto '{nome}' adicionado com sucesso.")
        