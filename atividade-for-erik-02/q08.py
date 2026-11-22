numeros = []

for i in range(10):
    n = int(input(f"Digite o {i + 1}º número: "))
    numeros.append(n)

busca = int(input("Digite um número para buscar: "))

contador = 0

for n in numeros:
    if n == busca:
        contador += 1

if contador == 0:
    print(f"O número {busca} não foi encontrado na lista.")
else:
    print(f"O número {busca} aparece {contador} vezes.")