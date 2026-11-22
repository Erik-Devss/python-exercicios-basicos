original = []
maiores_que_10 = []

for i in range(8):
    num = int(input(f"Digite o {i + 1}º número: "))
    original.append(num)

for num in original:
    if num > 10:
        maiores_que_10.append(num)

print(f"Lista original: {original}")
print(f"Números maiores que 10: {maiores_que_10}")