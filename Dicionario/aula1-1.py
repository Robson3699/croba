agenda={}
while True:
    nome=input("Digite seu nome:")
    while True:
     tel=input("infome seu telefone: ")
     try:
        tel_int=int(tel)    
        agenda [nome]=tel_int
        break
     except:
        print("digite um numero valido.")
    cpf=input("digite seu cpf: ")
    agenda ["cpf"]=cpf
    resp=input("voce deseja continuar add contatos: (s/n)")
    if(resp.lower()=='n'):
        print("saindo do programa")
        break
print(agenda)



