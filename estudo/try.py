while True:
 num=input("digite um numero ai amigo: ")

 try:
 
    num_float=float(num)
    l1= f'o dobro do seu numero eh {num_float*2:.2f}'
    print(l1)
    break
 except:

    print("codigo invalido")
 