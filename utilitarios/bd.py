import json
import os

ARQUIVO = "utilitarios.json"

def carregar_dados():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r") as f:
            return json.load(f)
    return {"usuarios":[],"produtos":[]}

def salvar_dados(dados):
    with open(ARQUIVO, "w") as f:
        json.dump(dados, f, indent=2)