numeros = []
positivos = []
negativos = []
zero = []

for i in range(10):
    n = int(input(f"Digite o {i + 1}º número: "))
    numeros.append(n)
    if n > 0:
        positivos.append(n)
    elif n < 0:
        negativos.append(n)
    else:
        zero.append(n)

print(f"Quantidade de positivos: {len(positivos)}")
print(f"Quantidade de negativos: {len(negativos)}")
print(f"Iguais a zero: {len(zero)}")
        