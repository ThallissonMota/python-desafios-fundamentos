# Lista de carros disponíveis
carros = ['BMW X6', 'BMW I5', 'BMW I8']

# Solicita ao usuário o carro desejado
procura = input("Qual carro você gostaria de comprar? ")

# Verifica se o carro informado está na lista
if procura in carros:
    print("O carro está disponivel")
else:
    print("O carro não está disponivel")
