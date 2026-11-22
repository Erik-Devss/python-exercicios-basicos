numeros = []

for i in range(8):
    num = int(input(f"Digite o {i + 1}º número: "))
    numeros.append(num)

tem_repetidos = False

for i in range(len(numeros)):
    for j in range(i + 1, len(numeros)):
        if numeros[i] == numeros[j]:
            tem_repetidos = True
            break
    if tem_repetidos:
        break


if tem_repetidos:
    print("Existem números repetidos.")
else:
    print("Não existem números repetidos.")