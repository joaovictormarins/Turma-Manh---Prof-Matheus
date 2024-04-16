valor = float(input('Digite um valor:'))
unidade_origem = input('Digite a unidade de origem desejada(Milhas,Polegadas,Pes,Centimetros,Metros ou Quilometros:)')
def converter(valor,unidade_origem):
 if unidade_origem == "Milhas":
    print(milhas =  valor)
    print(Polegadadas = valor*63360)
    print(Pes = valor*5280)
    print(Centimetros = valor*160934)
    print(Metros = valor*160934)
    print(Quilometros = valor*1.60934)
 elif unidade_origem == "Polegadas":
    print(milhas = valor/63360)
    print(Polegadas = valor)
    print(pes = valor/12)
    print(Centimetros = valor*2.54)
    print(Metros = valor*0.0254)
    print(Quilometros = valor*0.0000254)
 elif unidade_origem == "Pes":
    print(milhas = valor/5280)
    print(Polegadas = valor*12)
    print(Pes = valor)
    print(Centimetros = valor*30.48)
    print(Metros = valor*0.3048)
    print(Quilometros = valor*0.0000254)
 elif unidade_origem == "Centimetros":
    print(Milhas = valor/160934)
    print(Polegadas = valor/2.54)
    print(Pes = valor/30.48)
    print(Centimetros = valor)
    print(Metros = valor/100)
    print(Quilometros = valor/1000)
 elif unidade_origem == "Metros":
    print(Milhas = valor/1609.34)
    print(Polegadas = valor/0.0254)
    print(Pes = valor/0.3048)
    print(Centimetros = valor*100)
    print(Metros = valor)
    print(Quilometros = valor*1000)
 elif unidade_origem == "Quilometros":
    print(Milhas = valor/1.60934)
    print(polegadas = valor/0.0000254)
    print(Pes = valor/0.0003048)
    print(Centimetros = valor*10000)
    print(Metros = valor*1000)
    print(Quilometros = valor)
 else:
    print("Unidade de origem não corrspondida")
resultado = converter(valor,unidade_origem)
if (resultado,tuple):
   print('Milhas',)





