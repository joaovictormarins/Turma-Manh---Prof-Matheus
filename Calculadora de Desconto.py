#calculadora de desconto
preco_original = float(input("Digite o preço original do item especificado: "))

percentual_desconto = float(input("Digite o percentual de desconto (%): "))

desconto = (percentual_desconto / 100) * preco_original

preco_com_desconto = preco_original - desconto

print("Desconto: R$", desconto)
print("Preço com desconto: R$", preco_com_desconto)

