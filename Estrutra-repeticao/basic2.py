banho = tosa = banhotosa = outros = 0

for i in range (5):
  print("1- banho")
  print("2- tosa")
  print("3- banho e tosa")
  print("4- outros")


  op=input("informe o servico: ")
  op_int=int(op)

  match(op_int):
     case 1:
        banho=+1
     case 2:
        tosa+=1
     case 3:
        banhotosa+=1
     case 4:
        outros+=1    
        
print(banho)
print(banhotosa)
print(tosa)
print(outros)