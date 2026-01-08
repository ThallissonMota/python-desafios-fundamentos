# Lista de frutas
frutas = ['maca', 'abacate', 'banana']

# Lista de vegetais
vegetais = ['cenoura', 'couve', 'abobora']

# Nested for loop (for dentro de outro for)
# Usado quando é preciso comparar ou combinar listas
for fruta in frutas:          # Loop externo
    for vegetal in vegetais:  # Loop interno
        # Executa para cada combinação possível
        print(fruta, vegetal)
