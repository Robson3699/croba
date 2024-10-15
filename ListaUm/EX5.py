saldo=0.0
while(True):
   resP=int(input("Digite 1 para Saque \nDigite 2 para Deposito:"))
   if(resP==1):
      saque=input("quanto voce deseja sacar?: ")
      saque_float=float(saque)
      saldo=saldo-saque_float
      if(saldo<0 and saque_float>0):
         print("saque invalido seu saldo eh de",saldo)
         saldo=saldo+saque_float
      else:
         print("Seu saque foi efetuado com sucesso: ",saldo)
      resp=input("deseja continuar na opercao s/n: ")
      
      if(resp.lower()=='n'):
         break
   elif(resP==2):
      deposito=input("digite o valor de deposito: ")
      deposito_float=float(deposito)
      if(deposito_float>=0):
         saldo=saldo+deposito_float
         print("Deposito efetuado com sucesso: ",saldo)
      else:
         print("valor inserido invalido")
      resp=input("deseja continuar na opercao s/n: ")
      
      if(resp.lower()=='n'):
         break
         
      

      
      
           


    

    
    

