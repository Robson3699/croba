weight=float(input("whats your weight: "))
d=input("L(lbs) ou K(kg): ")

if d.upper()=="L" :
    lbs=weight*0.454
    print("your weight in KG is: " + str(lbs))
elif d.upper()=='K':
    kg=weight*2.204
    print("your weight in LBS is: "+ str(kg))
