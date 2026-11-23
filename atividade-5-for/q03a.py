impares = 0

for i in range(1, 51):
    if i % 2 != 0:
        impares = impares + 1
        print(i)
print("Total de números ímpares:", impares)