# Dicionário é uma estrutura que armazena dados no formato chave : valor
# Aqui, o país é a chave e a capital é o valor
cidades_capitais = {
    "Brasil": "Brasilia",
    "Itália": "Roma",
    "Russia": "Moscou",
    "Canada": "Ottawa",
    "Australia": "Canberra"
}

# Pede ao usuário o nome de um país (chave do dicionário)
capital = input("Digite o nome de um pais: ")

# Verifica se a chave existe dentro do dicionário
if capital in cidades_capitais:
    # Acessa o valor usando a chave entre colchetes
    print(f"A capital de {capital} é {cidades_capitais[capital]}")
    # [] é usado para acessar o valor associado à chave
else:
    # Executa se a chave não existir no dicionário
    print("Não temos informações sobre a capital desse pais")
