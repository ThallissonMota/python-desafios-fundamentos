# Função que calcula potência, com expoente padrão igual a 2
def expoente(a, b = 2):
    return a ** b  # Retorna a base elevada ao expoente

# Solicita a base
a = int(input("Digite a base: "))

# Solicita o expoente como string
# Se nada for digitado, o valor será vazio e não causará erro
b = input("Digite o expoente: ")

# Verifica se o usuário digitou algum valor para o expoente
if b:  # Se houver valor, converte para inteiro
    print(f"a raiz é {expoente(a, int(b))}")
else:  # Se não houver valor, usa o expoente padrão (2)
    print(f"a raiz é {expoente(a)}")
