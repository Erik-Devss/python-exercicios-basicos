idade = int(input("Digite sua idade: "))
if idade >=18:
    print("Pode entrar no evento.")
elif idade >= 16:
    print("Pode entrar no evento com autorização dos pais.")
else:
    print("Não pode entrar no evento.")
