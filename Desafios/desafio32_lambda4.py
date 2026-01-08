# Lista de números
lista = [1, 2, 3, 4, 5, 6, 7]

# Função lambda que calcula o quadrado de um número
quadrado = lambda num: num ** 2

# List comprehension aplica a função a cada item da lista
resultado = [quadrado(num) for num in lista]

# Exibe a nova lista com os valores ao quadrado
print(resultado)
