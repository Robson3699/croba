ageT=0
oW=0
wOverT=0
male=0
for i in range(5):
 sex=input("qual o seu sexo:(M/H) ")
 age=input("qual a sua idade: ")
 age_int=int(age)
 ageT=ageT+age_int
 if(sex.upper()=='H'):
  male+=1
 elif(sex.upper()=='M'):
  if(age_int>oW):
   oW=age_int
  if(age_int>20):
   wOverT+=1
print("homes cadastrados: ",male)
print("mulher mais velhas: ",oW)
print("media de todos: ", ageT/5)
print("mulheres acima de 20 anos: ", wOverT)
   

