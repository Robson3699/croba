wt=0
wm=0
for i in range (10):
 cont=input("quantos filhos voce tem? ")
 cont_int=int(cont)
 print(i)

 if(cont_int<=2):
  wt+=1
 else:
  wm+=1
  

print("o numero de mulheres com ate 2 filhos foi: ", wt)
print("o numero de mulheres com mais de 2 filhos foi: ", wm)
