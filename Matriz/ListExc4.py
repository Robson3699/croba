pro=input("quantos produtos foram vendidos?: ")
pro_int=int(pro)
weight = []
for i in range(pro_int):
   line1= f' digite o produto {i+1}: '
   weight.append(int(input(line1)))
print("o peso medio foi: ",sum(weight)/pro_int)
print("O maior peso vendido foi: ", max(weight))
print("O Menor peso vendido foi :", min(weight))
print("o Valor total arrecado foi",sum(weight)*4.35)