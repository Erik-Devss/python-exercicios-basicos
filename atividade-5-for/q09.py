positivos = 0
negativos = 0
igual_a = 0

for i in range(1, 11):
    n = int(input(f"Digite o {i}º número inteiro: "))
    if n > 0:
        positivos = positivos + 1
    elif n < 0:
        negativos = negativos + 1
    else:
        igual_a = igual_a + 1
        
print("Total de números positivos:", positivos)
print("Total de números negativos:", negativos)
print("Total de números iguais a zero:", igual_a)