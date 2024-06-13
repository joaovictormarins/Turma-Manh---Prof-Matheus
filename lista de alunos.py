alunos =  [] 
for _ in range (100):
    nome = input("Digite o nome do aluno (ou '0' para encerrar): ")
    if nome == "0":
        break 
    alunos.append(nome)
    print("Lista de alunos:")
    for aluno in alunos:
        print(aluno)

