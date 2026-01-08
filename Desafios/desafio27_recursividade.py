# Função fatorial usando recursividade
def fatorial(n):
    
    # Caso base: quando n é 0 ou 1, a função para
    if n == 0 or n == 1:
        return 1
    else:
        # Chamada recursiva: a função chama ela mesma
        return n * fatorial(n - 1)
    
# Chamada da função
print(fatorial(2))    

# Recursividade é quando uma função chama ela mesma
# Ela sempre precisa de um caso base para evitar loop infinito
