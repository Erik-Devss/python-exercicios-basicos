numeros = []
pares = []
impares = []

for i in range(10):
    n = int(input(f"Digite o {i + 1}º número: "))
    numeros.append(n)
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

print(f"Lista original: {numeros}")
print(f"Números pares: {pares}")
print(f"Números ímpares: {impares}")
