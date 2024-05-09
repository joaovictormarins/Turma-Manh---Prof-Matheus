Nota1 = float(input("Digite a Nota1:"))
Nota2 = float (input("Digite a Nota2:"))
Nota3 = float(input("Digite a Nota3:"))

Media = (Nota1 + Nota2 + Nota3)

if Media <= 7:
  print("Parabéns Você foi aprovado com Media:",Media)
else:
  print("Infelizmente, Você foi Reprovado com Media:",Media)