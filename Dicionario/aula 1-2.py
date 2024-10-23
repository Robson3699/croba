stq={}
while True:
    cm=input("digite o nome do produto: ")
    qtd=input("digite a qtd do produto: ")
    while True:
        try:
            qtd_int=int(qtd)
            stq [cm]=qtd_int
            break
        except:
            print("digite uma quatidade valida")
    rep=input("deseja continuar (s/n)")
    if(rep.lower()=='n'):
        break
print(stq)
    