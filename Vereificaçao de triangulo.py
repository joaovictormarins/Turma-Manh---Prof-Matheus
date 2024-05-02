r1 = float(input('primeiro segmento:'))
r2 = float(input('segundo segmento:'))
r3 = float(input('terceiro segmento:'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima podem formar um triangulo', end='')
    if r1 == r2 == r3:
        print('Equilátero!')
    elif r1 != r2 != r3 != r1:
        print('Escaleno!')
    else:
        print('Isósceles!')
else: 
    print('Os segmentos acima não podem formar um triangulo através dos critérios estabelecidos pelo usuário')
