numeros = []

while True:
    numero = int(input("Digite um número inteiro (digite 0 para parar): "))
    if numero == 0:
        break
    numeros.append(numero)

soma = sum(numeros)
print("A soma dos números digitados é:", soma)
