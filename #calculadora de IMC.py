#Calculadora de IMC
peso = float(input('Digite o seu peso:'))
altura = float(input('Digite a sua altura:'))
IMC = (peso/(altura*altura))
print('O IMC dessa pessoa é de {:.1f}'.format(IMC))
if IMC < 18.5: 
    print('Está abaixo do peso normal')
elif 18.5 <= IMC < 25:
    print('Parabéns os eu peso está na faixa normal')
elif 25 <= IMC < 30:
    print('Está em sobrepeso')
elif 30 <= IMC < 40:
    print('Está em obesidade')
elif IMC >= 40: 
    print('Está em obesedade mórbida')