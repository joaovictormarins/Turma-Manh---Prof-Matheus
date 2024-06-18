#Função para verificar CPF's

def validar_cpf(cpf):
    #tirando pontos,espaços,itens indesejados
    #replace vai substituir 
    cpf = cpf.replace(".","").replace("-","").replace(" ","")
    #conferindo se os digitos são iguais a 11 e se não contem letras
    if not cpf.isdigit() or len(cpf) != 11:
        print("CPF são um conjunto de numeros de 11 digitos")
        return False
    return True 
#criando uma condição que rode enquanto o usuario não colocar 
# um CPF VALIDO 
 
