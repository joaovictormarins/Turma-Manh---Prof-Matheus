#Calculadora simples
n1 = float (input("Digite um número:"))
operacao = input("Digite o sinal da operação:")
n2 = float (input("Digite outro número:"))

if operacao == "+":
    resultado = n1 + n2 
elif operacao == "-":
    resultado = n1 - n2 
elif operacao == "/":
    resultado = n1 / n2 
elif operacao == "**":
    resultado = n1 ** n2 
elif operacao == "*":
    resultado = n1 * n2 
else:
    resultado = "operação inválida"
print(str (n1)+ '' + str (operacao) + '' + str (n2) + "=" + str (resultado))