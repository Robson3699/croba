while True:
    pH=input("digite o ph da agua ai minha consagrada: (-1 sair) ")
    pH_float=float(pH)
    if(pH_float==-1):
        break
    elif(pH_float>=0 and pH_float<7):
        print("acida")
    elif(pH_float==7):
        print("neutra")
    else:
        print("basica")
