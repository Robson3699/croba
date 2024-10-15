while(True):
    inv=input("quanto voce quer investir: ")
    jur=input("qual a taxa de juros: ")
    time=input("quanto tempo: ")
    inv_float=float(inv)
    jur_float=float(jur)
    time_int=int(time)

    for i in range(time_int):
        inv_float=inv_float+inv_float*(jur_float/100)
        print("seu o investimento ao final do ano:",i+1,"rendeu: ",inv_float)
    resp=input("quer continuar a simulacao (S/N): ")
    if(resp.upper()=='N'):
        break
 