aluno = input("Digite o nome do aluno: ")
faltas = int(input("Digite o número de faltas: "))
if faltas > 10:
    print(f"O aluno {aluno} está acima do limite de faltas. Número de faltas: {faltas}.")
elif faltas == 10:
    print(f"O aluno {aluno} está no limite de faltas.")
else:
    print(f"O aluno {aluno} está abaixo do limite de faltas. Número de faltas: {faltas}.")
