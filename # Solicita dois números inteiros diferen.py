# Solicita dois números inteiros diferentes do usuário
num1 = float(input("Digite o primeiro número inteiro: "))
num2 = float(input("Digite o segundo número inteiro: "))

# Verifica se os números são diferentes
if num1 == num2:
    print("Os números fornecidos são iguais. Por favor, forneça dois números diferentes.")
else:
    # Classifica os números em ordem crescente
    if num1 < num2:
        menor = num1
        maior = num2
    else:
        menor = num2
        maior = num1

    # Exibe os números em ordem crescente
    print("Os números em ordem crescente são:", menor, ",", maior)

