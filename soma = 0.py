soma = 0
atribuidor = 0 
while True:
    numero = int(input("Digite um número inteiro (digite 0 para parar): "))
    if numero == 0:
        break
    soma  = numero + soma 
    atribuidor += 1 
print("A soma dos números digitados é:", soma)
