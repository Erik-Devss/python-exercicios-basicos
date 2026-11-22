maior = []
posicao = []

for i in range(8):
    n = int(input(f"Digite o {i + 1}º número: "))
    if n > maior:
        maior.append(n)
        posicao.append(i + 1)

print(f"O maior número digitado foi: {maior} ")
print(f"Posição: {posicao} ")