numero = int(input('Digite um número qualquer'))
resultado =(numero)
print 
(resultado)
if numero > 0 and numero % 2 == 0:
    print('resultado = Positivo e Par')
elif numero > 0 and numero % 3 == 0:
    print('resultado = numero Positivo e Múltiplo de 3')
elif numero < 0 and numero % 2 == 0:
    print('resultado = numero Negativo e Ímpar')
elif numero == 0:
    print('zero')
else:
    print('Nenhuma das condições estabelecidas')

