compras = ['leite', 'couve', 'tomate', 'garfo', 'faca', 'refrigerante']
bebidas = ['uva', 'colher', 'vinho', 'cerveja', 'banana']
talheres = ['arroz', 'concha', 'whisky', 'vodka', 'feijao', 'colher de chá']

compras.remove('garfo')
compras.remove('faca')
compras.remove('refrigerante')
compras.extend(['banana', 'uva', 'arroz', 'feijao'])

bebidas.remove('uva')
bebidas.remove('banana')
bebidas.remove('colher')
bebidas.extend(['refrigerante', 'whisky', 'vodka'])

talheres.remove('arroz')
talheres.remove('whisky')
talheres.remove('vodka')
talheres.remove('feijao')
talheres.extend(['garfo', 'faca', 'colher', 'concha', 'colher de chá'])

print("Lista de compras:", compras)
print("Lista de bebidas:", bebidas)
print("Lista de talheres:", talheres)
