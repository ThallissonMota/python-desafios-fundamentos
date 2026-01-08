# Set é uma coleção de dados NÃO ordenada e SEM valores duplicados
# Usa {} e é ideal para operações matemáticas como união e interseção
list01 = {"Marcos", "Felipe", "Amanda", "Karol", "Antonio"}
list02 = {"Francisco", "Maria", "Joao", "Marcos", "Amanda"}

# intersection retorna apenas os elementos que existem nos dois sets
set01 = list01.intersection(list02)  # Vai mostrar o que tem em comum entre eles

# Exibe o resultado da interseção
print(set01)
