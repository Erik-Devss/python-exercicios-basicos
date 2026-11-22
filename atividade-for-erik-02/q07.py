numeros = []

for i in range(10):
    num = int(input(f"Digite o {i + 1}º número: "))
    numeros.append(num)

soma_pares = 0
soma_impares = 0

for num in numeros:
    if num % 2 == 0:
        soma_pares = soma_pares + num
    else:
        soma_impares = soma_impares + num


print(f"Lista digitada: {numeros}")
print(f"Soma dos pares: {soma_pares}")
print(f"Soma dos ímpares: {soma_impares}")