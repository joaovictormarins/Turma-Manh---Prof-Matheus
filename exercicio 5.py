
print("Digite os elementos da lista separados por espaços:")
entrada = input() 
elementos = []

numero_str = ''

for char in entrada + ' ':  
    if char != ' ':
        numero_str += char
    else:
        if numero_str != '':
            elementos.append(float(numero_str))
            numero_str = ''

lista_sem_duplicatas = []

for elemento in elementos:
    if elemento not in lista_sem_duplicatas:
        lista_sem_duplicatas.append(elemento)
print("Lista sem duplicatas:", lista_sem_duplicatas)
