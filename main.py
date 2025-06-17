import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent))

from utilitarios.bd import *
from utilitarios.auth import *
from utilitarios.crud import *
from utilitarios.interface import *
from utilitarios.produtos import *
from utilitarios.usuarios import *

def main():
    carregar_dados()
    while True:
        opcao_1 = menu_cadastro()
        
        if opcao_1 =='1':
            cadastrar_usuario()
          
        elif opcao_1=='2':
            if login_user():
                # Área restrita - só entra aqui se o login for bem-sucedido
                print("Acesso ao sistema concedido.")
        elif opcao_1=='3':
            break
        







if __name__=="__main__":
    main()