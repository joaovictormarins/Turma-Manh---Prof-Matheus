#conversor de nota em conceito
nota = float(input("Digite a nota do aluno: "))

if nota >= 9:
    conceito = 'A'
elif nota >= 7.5:
    conceito = 'B'
elif nota >= 6:
    conceito = 'C'
elif nota >= 4:
    conceito = 'D'
else:
    conceito = 'F'

print("Conceito correspondente:", conceito)
