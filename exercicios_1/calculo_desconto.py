valor_produto = float(input("Digite o valor do produto: R$ "))
percentual_desconto = float(input("Digite o percentual de desconto (%): "))

valor_final = valor_produto * (1 - (percentual_desconto / 100))
print("O produto com", percentual_desconto, "% de desconto custará: R$ ", valor_final)