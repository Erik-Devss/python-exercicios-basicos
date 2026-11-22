nomes = []
notas = []

for i in range(5):
    nome = input(f"Digite o nome do {i + 1}º aluno: ")
    nota = float(input(f"Digite a nota de {nome}: "))
    nomes.append(nome)
    notas.append(nota)

for i in range(len(nomes)):
    if notas[i] >= 7:
        situacao = "Aprovado"
    else:
        situacao = "Reprovado"

    print(f"Aluno: {nomes[i]}")
    print(f"Nota: {notas[i]}")
    print(f"Situação: {situacao}")