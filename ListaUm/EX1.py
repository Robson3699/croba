val=input("quanto custa a bolsa?")
val_int=int(val)

print("o valor a vista com desconto de 10%:",val_int*1.1,"Reais")
print("parcelado em 1+2x sem desconto","tres parcelas de ",val_int/3)
print("dividido em 10x com 5 de juros",(val_int+val_int*0.05)/10,"reais")