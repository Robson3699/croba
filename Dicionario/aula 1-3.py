carro={}
while True:
    marca=input("digite o nome do modelo: ")
    while True:
        qtd=input("digite e o ano: ")
        try:
            qtd_int=int(qtd)
            carro [marca]=qtd_int
            break
        except:
            print("digite uma quatidade valida")
    print(carro.keys(),carro[marca])
    
    rep=input("deseja continuar (s/n)")
    if(rep.lower()=='n'):
        break
print(carro)
