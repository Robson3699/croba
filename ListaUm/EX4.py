name=input("digite eu nome: ")
notaUm=input("digite sua nota de qualidade ")
notaDois=input("digite sua nota 2 assiduidedade")
notaTres=input("digite sua nota 3 comportamento")

media=(float(notaUm)*2+float(notaDois)*3+float(notaTres)*5)/10

if(media<=4.9):
    print("ta uma merda")
elif(media>=5 and media<=6.9):
    print("ta bom")
else:
    print("brabo")
