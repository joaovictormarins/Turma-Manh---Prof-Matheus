# Solicita ao usuário que digite um número inteiro positivo
numero = int(input("Digite um número inteiro positivo: "))
soma_divisores = 0

for i in range(1, numero):
    if numero % i == 0:
        soma_divisores += i

if soma_divisores == numero:
    print(f"O número {numero} é um número perfeito.")
else:
    print(f"O número {numero} não é um número perfeito.")
