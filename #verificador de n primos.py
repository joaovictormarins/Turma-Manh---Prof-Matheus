#verificador de n primos
numero = float(input("Digite um número inteiro positivo maior que 1: "))

if numero <= 1:
    print("Número inválido. Digite um número inteiro positivo maior que 1.")
else:
    primo = True
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            primo = False
            break
    
    if primo:
        print(f"O número {numero} é primo.")
    else:
        print(f"O número {numero} não é primo.")
