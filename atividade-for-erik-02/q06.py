lista = []

for i in range(7):
    num = int(input(f"Digite o {i + 1}º número: "))
    lista.append(num)

invertida = []


for i in range(len(lista) - 1, -1, -1):
    invertida.append(lista[i])


print(f"Lista original: {lista}")
print(f"Lista invertida: {invertida}")