acumulador=0
while True:
    num=input("informe o numero(0-Sair): ")
    num_int=int(num)
    if(num_int<0):
        print("informe outro numero")
    elif(num_int==0):
        break
    else:
        acumulador+=num_int

print(acumulador)
        