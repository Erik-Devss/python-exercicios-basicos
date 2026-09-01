nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
media = (nota1 + nota2 + nota3) / 3
nome = input("Digite o nome do aluno: ")

if media >= 7:
    print(f"O aluno {nome} está aprovado.")
elif media >= 5:
    print(f"O aluno {nome} está em recuperação.")
else:
    print(f"O aluno {nome} está reprovado.")
