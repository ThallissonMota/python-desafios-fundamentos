# Lista inicial de frutas
frutas = ['maçã', 'banana', 'manga', 'uva']

# Altera o item do índice 1
frutas[1] = "morango"

# Adiciona um item ao final da lista
frutas.append("abacaxi")

# Exibe a lista atualizada
print(frutas)

# Altera vários itens usando fatiamento (índices 1 e 2)
frutas[1:3] = ['x', 'y']  # O último índice não é incluído

# Exibe a lista após o fatiamento
print(frutas)

# Insere um item no índice 1 sem remover os outros
frutas.insert(1, "abacate")
