while True:
 val=input("digite o valor total das compras (0-sair): ")
 val_float=float(val)

 if(val_float>100):
  print("voce obeteve um desconto",val_float-+val_float*0.10)
 elif(val_float>0 and val_float<=100):
  print("sem desconto", val_float)
 elif(val_float==0):
  break


