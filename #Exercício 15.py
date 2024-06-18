#Exercício 15 
comidas = ["leite","couve","computador","tomate","garfo","faca","tablet","refrigerante"]
bebidas = ["uva","colher","tv","vinho","cerveja","celular","banana"]
talheres = ["arroz","iphone","concha","whisky","vodka","feijão","colher de chá"]
eletronicos = []

comidas.remove('garfo')
comidas.remove("computador")
comidas.remove("tablet")
comidas.remove('faca')
comidas.remove('refrigerante')
comidas.extend(['banana', 'uva', 'arroz', 'feijao'])

bebidas.remove("colher")
bebidas.remove("tv")
bebidas.remove("celular")
bebidas.remove("banana")
bebidas.remove("uva")
bebidas.extend(["leite","refrigerante","whisky","vodka"])

talheres.remove("arroz")
talheres.remove("iphone")
talheres.remove("whisky")
talheres.remove("vodka")
talheres.remove("feijão")
talheres.extend(["colher","garfo","faca"])

eletronicos.extend(["computador","tablet","tv","celular","iphone"])

print("lista de comidas:" , comidas)
print("lista de bebidas:" , bebidas)
print("lista de talheres:" , talheres)
print("lista de eletronicos:" , eletronicos)
      

