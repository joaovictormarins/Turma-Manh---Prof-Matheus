#Código para Gerar a Sequência de Fibonacci
fibonacci = [0, 1]
quantidade = int(input("Digite a quantidade de números da sequência de Fibonacci a ser gerada: "))

for i in range(2, quantidade):
    proximo = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(proximo)
print(f"Sequência de Fibonacci com {quantidade} números:")
print(fibonacci)
