# Lista com frutas (valores repetidos)
frutas = ['maca', 'abacate', 'maca', 'banana', 'maca', 'morango']

# Variável usada para contar ocorrências
contador = 0

# Percorre cada item da lista
for fruta in frutas:
    # Verifica se a fruta é "maca"
    if fruta == "maca":
        contador += 1  # Soma 1 ao contador

# Exibe a quantidade encontrada
print(contador)
