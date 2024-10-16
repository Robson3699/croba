num=input("digita um numero ai: ")
try:
    num_int=int(num)
    if(type(num_int)==int):
        if(num_int%2==0):
            print("o numero eh pa")
        else:
            print("numero eh impar")
    
except:
    print("digitou errado ai")

name=input("digita teu primeiro nome: ")
if(len(name)<=4):
    print("nome curto")
elif(len(name)>4 and len(name)<=6):
    print("nome normal")
else:
    print("nome grande da porra")