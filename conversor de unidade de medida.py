
unidade_origem = input('Escreva a uidade de medida desejada(Milhas,Polegadas,Pes,Centimetros,Metros ou Quilometros:)')
valor = float(input('Escreva o valor a ser convertido:'))

if unidade_origem == 'Milhas'or'milhas':
    print('Milhas =',valor)
    print('Polegadas =', valor*63360)
    print('Pes =', valor*5280)
    print('Centimetros =', valor*160934)
    print('Metros =', valor*160934)
    print('Quilometros =', valor*1.60934)
elif unidade_origem == 'Polegadas'or'polegadas':
    print('Milhas =', valor/63360)
    print('Polegadas =', valor)
    print('Pes =', valor/12)
    print('Centimetros =', valor*2.54)
    print('Metros =', valor*0.0254)
    print('Quilometros =', valor*0.0000254)
elif unidade_origem =='Pes'or'pes':
    print('Milhas =', valor/5280)
    print('Polegadas =', valor*12)
    print('Pes =', valor)
    print('Centimetros =', valor*30.48)
    print('metros =', valor*0.3048)
    print('Quilometros =', valor*0.0000254)
elif unidade_origem == 'Centimetros'or'centimetros':
    print('Milhas =', valor/160934)
    print('Polegadas =', valor/2.54)
    print('Pes =', valor/30.48)
    print('Centimetros =', valor)
    print('Metros =', valor*100)
    print('Quiometros =', valor/1000)
elif unidade_origem == 'Metros'or'milhas':
    print('Milhas =',valor/1609.34)
    print('Polegadas =', valor/0.0254)
    print('Pes = ', valor/0.3048)
    print('Centimetros =', valor*100)
    print('Metros =', valor)
    print('Quilometros =', valor*1000)
elif unidade_origem == 'Quilometros'or'quilometros':
    print('Milhas =', valor/1.60934)
    print('Polegadas =', valor/0.0000254)
    print('Pes =', valor/0.0003048)
    print('Centimetros =', valor*10000)
    print('Metros =', valor*1000)
    print('Quilometros =', valor)
else:
    print('Unidade de origem não corresponde')