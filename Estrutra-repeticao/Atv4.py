while True:
    pHome=input("digite o valor da casa do seus sonhos ai camarada: ")
    pHome_float=float(pHome)
    income=input("digita teu salario ai amigo: ")
    income_float=float(income)
    time=input("digita em quanto tempo tu quer pagar saporra: ")
    time_int=int(time*12)

    can=income_float*0.3
    if(income_float/time_int>can):
        print("nao vai dar para te ajudar amigo, procura uma casa mais barata ou ganha mais")
        op=input("quer para de simular (0-Sair)")
        op_int=int(op)
        if(op_int==0):
            break;
    elif(income_float/time_int<can):
        print("ta aprovada essa casa ai seu pobre")
        op=input("quer para de simular (0-Sair)")
        op_int=int(op)
        if(op_int==0):
            break;
        
    
    


        
