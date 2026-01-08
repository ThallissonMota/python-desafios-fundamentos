# input() captura dados digitados pelo usuário (sempre texto)
nome = input("Qual o seu nome? ")

# Mesmo números entram como string
idade = input("Qual sua idade? ")

# format() substitui {} pelos valores das variáveis
print("Olá, {}! Você tem {} anos".format(nome, idade))
