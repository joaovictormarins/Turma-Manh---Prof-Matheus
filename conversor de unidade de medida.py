
# Conversor de Unidade De Medida
valor = float(input("Digite o valor a ser convertido: "))
unidade_origem = input("Digite a unidade de medida (Milhas, Polegadas, Pés, Centímetros, Metros ou Quilômetros): ").lower()


fatores = {
    'milhas': {'polegadas': 63360, 'pés': 5280, 'centímetros': 160934, 'metros': 1609.34, 'quilômetros': 1.60934},
    'polegadas': {'milhas': 1 / 63360, 'pés': 1 / 12, 'centímetros': 2.54, 'metros': 0.0254, 'quilômetros': 2.54e-5},
    'pés': {'milhas': 1 / 5280, 'polegadas': 12, 'centímetros': 30.48, 'metros': 0.3048, 'quilômetros': 0.0003048},
    'centímetros': {'milhas': 6.2137e-6, 'polegadas': 0.393701, 'pés': 0.0328084, 'metros': 0.01, 'quilômetros': 1e-5},
    'metros': {'milhas': 0.000621371, 'polegadas': 39.3701, 'pés': 3.28084, 'centímetros': 100, 'quilômetros': 0.001},
    'quilômetros': {'milhas': 0.621371, 'polegadas': 39370.1, 'pés': 3280.84, 'centímetros': 100000, 'metros': 1000}
}

if unidade_origem in fatores:
    
    print(f"Conversões de {valor} {unidade_origem}:")
    for unidade_destino, fator in fatores[unidade_origem].items():
        resultado = valor * fator
        print(f"{resultado} {unidade_destino}")
else:
    print("Unidade de medida inválida.")