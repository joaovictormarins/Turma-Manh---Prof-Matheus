#Simulação De uma fila De Atendimento

fila_atendimento = []


while True:
    print("\nEscolha uma opção:")
    print("1. Adicionar cliente")
    print("2. Atender cliente")
    print("3. Ver fila de atendimento")
    print("4. Sair do programa")
    opcao = input("Digite o número da opção desejada: ")

    if opcao == '1':
        cliente = input("Digite o nome do cliente a ser adicionado: ")
        fila_atendimento.append(cliente)
        print(f"Cliente '{cliente}' adicionado ao final da fila.")

    
    elif opcao == '2':
        if fila_atendimento:
            cliente_atendido = fila_atendimento.pop(0)
            print(f"Cliente '{cliente_atendido}' foi atendido e removido da fila.")
        else:
            print("Não há clientes na fila para atender.")


    elif opcao == '3':
        print("Fila de atendimento:", fila_atendimento)


    elif opcao == '4':
        print("Encerrando o programa.")
        break

    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")



