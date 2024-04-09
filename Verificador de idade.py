print("=" * 20)
print("Verifique sua idade")
print("=" * 20)
idade_pessoa = int(input('Digite a sua idade:'))
if idade_pessoa <= 10:
    print('Voce é uma criança')
elif idade_pessoa >= 11 and idade_pessoa <= 14:
    print('Voce é um pré-adolescente')
elif idade_pessoa >= 15 and idade_pessoa <= 18:
    print('Voce é um adolescente')
elif idade_pessoa >= 19 and idade_pessoa <= 40:
    print('Voce é um jovem adulto')
else:
    print('voce é um idoso')
