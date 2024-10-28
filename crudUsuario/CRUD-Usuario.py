import json
import os
##from time import sleep


class cor:
    VERMELHO = '\033[91m'
    VERDE = '\033[92m'
    AMARELO = '\033[93m'
    AZUL = '\033[94m'
    MAGENTA = '\033[95m'
    CIANO = '\033[96m'
    RESET = '\033[0m'


# Definindo o caminho do arquivo no escopo global
arquivo = os.path.join(os.path.dirname(__file__), 'usuarios.json')


def carregar_usuarios():
    # Verifica se o arquivo existe, se não existir, cria um arquivo com lista vazia
    if not os.path.exists(arquivo):
        with open(arquivo, 'w') as f:
            json.dump([], f, indent=5)
    
    # Carrega o conteúdo do arquivo
    with open(arquivo, 'r') as f:
        return json.load(f)

def adicionar_usuario(nome, idade, cpf):
    usuarios = carregar_usuarios()
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            return print("USUARIO JA CADASTRADO!")

    usuarios.append({'nome': nome, 'idade': idade, 'cpf': cpf})

    with open(arquivo, 'w') as f:
        json.dump(usuarios, f, indent=5, ensure_ascii=False)
    print("😎 USUÁRIO ADICIONADO COM SUCESSO!")
    
def listar_usuarios():
    usuarios = carregar_usuarios()

    if usuarios:
        print("=" *50)
        print("LISTA DE USUÁRIOS:")
        print("-" *50)
        for usuario in usuarios:
            print("*" *50)
            print(f"NOME: {usuario['nome']}, IDADE: {usuario['idade']}, CPF: {usuario['cpf']}")
            print("*" *50)
            print("=" *50)
    else:
        print("😒 NENHUM USUÁRIO CADASTRADO.")

def atualizar_usuario(cpf_antigo, novo_nome, nova_idade, novo_cpf):
    usuarios = carregar_usuarios()

    for usuario in usuarios:
        if usuario['cpf'] == cpf_antigo:
            usuario['nome'] = novo_nome
            usuario['idade'] = nova_idade
            usuario['cpf'] = novo_cpf
            break

    with open(arquivo, 'w') as f:
        json.dump(usuarios, f, indent=5, ensure_ascii=False)
    print("😙 USUÁRIO ATUALIZADO COM SUCESSO!")

def excluir_usuario(cpf):
    usuarios = carregar_usuarios()

    for usuario in usuarios:  
        if usuario['cpf'] == cpf:
            usuarios.remove(usuario)

    with open(arquivo, 'w') as f:
        json.dump(usuarios, f, indent=5, ensure_ascii=False)
    print("😡 USUÁRIO EXCLUÍDO COM SUCESSO!")

def buscar_usuario(cpf):
    usuarios = carregar_usuarios()
    
    encontrado = False

    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            print(f"NOME: {usuario['nome']}, IDADE: {usuario['idade']}, CPF: {usuario['cpf']}")
            encontrado = True
    if not encontrado:
        print("😒 NENHUM USUÁRIO CADASTRADO.")
    

def linha_horizontal(cor):
    return cor + "=" * 50 + cor['RESET']

def menu_inicial():
    print(cor.CIANO + "=" *55 + cor.RESET)
    print(cor.VERMELHO + " ---->>> BEM VINDO AO SISTEMA MERCADO CLEAN <<<---- ")
    print("          1 - MÓDULO USUÁRIO ")
    print("          2 - MÓDULO ESTOQUE ")
    print("          3 - SAIR ")
    print(cor.CIANO + "=" *55 + cor.RESET)
    
def exibir_menu():
    print("\nMENU:")
    print("1. ADICIONAR USUÁRIO")
    print("2. LISTAR USUÁRIOS")
    print("3. ATUALIZAR USUÁRIO")
    print("4. EXCLUIR USUÁRIO")
    print("5. LISTAR UM USUÁRIO")
    print("6. VOLTAR AO MENU ANTERIOR")


def main():
    
    while True:
        menu_inicial()
        opcao_inicial = int(input("INFORME UMA OPÇÃO: "))

        match (opcao_inicial):
            case 2:
                print("MÓDULO EM DESENVOLVIMENTO")

            case 1:
                while True: 
                    exibir_menu()
                    opcao = input("ESCOLHA UMA OPÇÃO:\n>>>")

                    if opcao == "1":
                        nome = input(" DIGITE O NOME:\n>>>")
                        idade = input(" DIGITE A IDADE:\n>>>")
                        cpf = input(" DIGITE O CPF:\n>>>")
                        adicionar_usuario(nome, idade, cpf)
                    elif opcao == "2":
                        listar_usuarios()
                    elif opcao == "3":
                        cpf_antigo = input("DIGITE O CPF A SER ATUALIZADO:\n>>>")
                        novo_nome = input("DIGITE O NOVO NOME:\n>>>")
                        nova_idade = input("DIGITE A NOVA IDADE:\n>>>")
                        novo_cpf = input("DIGITE O NOVO CPF:\n>>>")
                        atualizar_usuario(cpf_antigo, novo_nome, nova_idade, novo_cpf)
                    elif opcao == "4":
                        cpf = input("DIGITE O CPF DO USUÁRIO A SER EXCLUÍDO:\n>>>")
                        excluir_usuario(cpf)
                    elif opcao == "5":
                        cpf = input("DIGITE O CPF DO USUÁRIO:\n>>>")
                        buscar_usuario(cpf)
                    elif opcao == "6":
                        print("VOLTAR AO MENU ANTERIOR...")
##                        sleep(3)
                        break
                    else:
                        print("😡 OPÇÃO INVÁLIDA. TENTE NOVAMENTE!")
            case 3:
                print("🚀 SAINDO...")
 ##               sleep(3)
                break
            case __:
                print("😡 OPÇÃO INVÁLIDA. TENTE NOVAMENTE!")

if __name__ == "__main__":
    main()
