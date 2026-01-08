# Lista de números para verificação
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Percorre cada número da lista
for numero in numeros:
    # Calcula o resto da divisão por 2
    par_impar = numero % 2
    
    # Se o resto for 0, o número é par
    if par_impar == 0:
        print(f"O número {numero} é par")
    else:
        print(f"O numero {numero} é impar")
