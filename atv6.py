def menu():
    print("1 - Bateria - 200,00$")
    print("2 - Pneu - 350,00$")
    print("3 - Filtro de Oleo - 50,00$")
    print("4 - Pastilha de Freio - 100,00$")
    print("5 - Opcao Invalida")

def nome_sistema():
    print(" Oficina do Seu joao ")

def op():
    op=input("escolha uma opcao: ")
    op_int=int(op)
    match (op_int):
        case 1:
            qtd=input("quantas baterias voce quer? ")
            qtd_int=int(qtd)
            if(qtd_int==0):
                print("qtd invalida")
            else:
                print("o Valor para" ,qtd_int, "baterias foi de", qtd_int*200,"Reais")
        case 2:
            qtd=input("quantos pneus voce quer? ")
            qtd_int=int(qtd)
            if(qtd_int==0):
                print("qtd invalida")
            else:
                print("o Valor para" ,qtd_int, "penus foi de", qtd_int*350,"Reais")
        case 3:
            qtd=input("quantos filtros de oleo voce quer? ")
            qtd_int=int(qtd)
            if(qtd_int==0):
                print("qtd invalida")
            else:
                print("o Valor para" ,qtd_int, "Filtro de oleo foi de", qtd_int*50,"Reais")
        case 4:
            qtd=input("quantas pastilhas de freio voce quer? ")
            qtd_int=int(qtd)
            if(qtd_int==0):
                print("qtd invalida")
            else:
                print("o Valor para" ,qtd_int, "pastilha de freio foi de", qtd_int*100,"Reais")
        case __:
            print("Opcao invalida")
            main()
def main():
    nome_sistema()
    menu()
    op()
if __name__ == '__main__':
    main()

            


