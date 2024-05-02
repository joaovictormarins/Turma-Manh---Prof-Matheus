preco = float(input('Qual é  preço inicial do produto? R$'))
novo = preco - (preco * desconto / 100)
print('O produto que custava R${}, na promoção com desconto de %{} vai custar R${}'.format(preco,novo))
