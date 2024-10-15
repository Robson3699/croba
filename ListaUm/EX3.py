ageP=input("inform age of property: ")
ageP_int=int(ageP)
if(ageP_int<=10):
    print("Seu Imovel eh novo")
elif(ageP_int>=11 and ageP_int<=30):
    print("Seu Imovel eh moderadamente antigo")
else:
    print("seu Imovel eh antigo")