agenda={}
while True:
    nome=input("Digite seu nome:")
    tel=input("infome seu telefone: ")
    try:
        tel_int=int(tel)    
        agenda [nome]=tel_int
    except:
        print("digite um numero valido.")
    cpf=input("digite seu cpf: ")
    agenda [nome]=cpf
    resp=input("voce deseja continuar add contatos: (s/n)")
    if(resp.lower()=='n'):
        print("saindo do programa")
        break
print(agenda)


