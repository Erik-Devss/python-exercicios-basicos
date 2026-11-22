notas = []
acima = []

for i in range(6):
    nt = float(input(f"Digite a {i + 1}ª nota: "))
    notas.append(nt)
    if nt >= 7.0:
        acima.append(nt)

print(f"Notas digitadas: {notas}")
print(f"Notas acima da média: {acima}")