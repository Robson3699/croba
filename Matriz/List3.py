list = [[],[]]

for rows in range(2):
    for coluns in range(2):
        list[rows].append(int(input("digite o valor: ")))
        print(list)

print(list)
print(list[0][1],list[1][0])