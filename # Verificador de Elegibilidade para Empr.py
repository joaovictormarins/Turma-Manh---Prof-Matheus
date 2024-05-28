# Verificador de Elegibilidade para Emprego
idade=float(input("Digite o sua idade:"))
nacionalidade=(input("Digite a sua nacionalidade:"))
anos_de_experiencia=float(input("Digite os anos de experiencia:"))

if idade >= 18 and anos_de_experiencia >= 2:

    if nacionalidade == "Brasileiro" or "Brasileira":
        print("Você está nos critérios elegivéis para vaga de emprego")
else:
    print("Você não é elegível para a vaga de emprego!")

    

