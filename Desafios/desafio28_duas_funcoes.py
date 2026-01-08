# Função que calcula o dobro de um valor
def dobro(valor2):
    return valor2 * 2  # Retorna o valor multiplicado por 2

# Função que calcula o quadrado usando outra função
def quadrado(valor2):
    return dobro(valor2) ** 2  # Reutiliza a função dobro

# Chamada da função quadrado
print(quadrado(2))
