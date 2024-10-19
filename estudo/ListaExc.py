listaDeCompras =[]

while True:   
     op=input('selecione uma opcao \n'+'[i]nserir [a]pagar [l]istar [s]air: ')
     if(op == 'i'):
      listaDeCompras.append(input("o que voce quer adicinar na lista: "))
      print("item adicionado com sucesso")
     elif(op== 'a'):
        id=input("digite o que voce quer remover da lista: ")
        id_int=int(id)
        listaDeCompras.pop(id_int)
        print("item apagado com sucesso")
     elif( op=='l'):
        for item in enumerate(listaDeCompras):
           print(item)
     elif(op=='s'):
        break
    
    

    