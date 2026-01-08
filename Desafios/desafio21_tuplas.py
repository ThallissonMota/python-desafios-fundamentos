# Tupla de cidades (estrutura imutável, não pode ser alterada)
cidades = ("São Paulo", "Rio de Janeiro", "Salvador")

# Solicita ao usuário uma cidade para verificação
tupla = input("Qual cidade você deseja visitar? ")

# Verifica se a cidade informada existe dentro da tupla
if tupla in cidades:
    print("A cidade está na lista de cidades")
else:
    print("A cidade não está na lista de cidades")
