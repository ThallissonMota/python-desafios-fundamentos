# Define uma função que realiza a soma de dois números
def soma():
    
    # Solicita o primeiro número e converte para inteiro
    a = int(input("Digite o primeiro numero: "))
    
    # Solicita o segundo número e converte para inteiro
    b = int(input("Digite o segundo numero: "))

    # Realiza a soma dos valores
    resultado = a + b

    # Exibe o resultado da soma
    print(f"O resultado da soma é {resultado}")

# Chamada da função para executar a soma
soma()
