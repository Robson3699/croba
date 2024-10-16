list=[]
while True:
    list.append(int(input("digite um numero ai: (0-Sair)")))
    if 0 in list:
        list.pop()
        break
print(list)