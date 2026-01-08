# Função lambda é uma função pequena e anônima (sem nome definido com def)
# Sintaxe: nome_da_funcao = lambda parametro: expressão
cubo = lambda x: x ** 3

# Chamada da função lambda
print(cubo(2))

# A palavra lambda substitui o uso do def em funções simples
# "cubo" passa a ser a referência da função
# "x" é o parâmetro recebido
# Ideal para funções curtas e rápidas
