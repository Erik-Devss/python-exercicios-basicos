n = 0

for i in range(1, 201):
    if i % 5 == 0:
        n = n + 1
        print(i)
        
print("Total de números divisíveis por 5 de 1 a 200:", n)