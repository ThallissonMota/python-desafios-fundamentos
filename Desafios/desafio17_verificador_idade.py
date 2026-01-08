# Solicita a idade do usuário e converte para inteiro
idade = int(input("Digite sua idade: "))

# Verifica se a idade é menor que 13
if idade < 13:
    print("Você é uma criança")

# Verifica se a idade está entre 13 e 19
elif 13 <= idade <= 19:
    print("Você é um adolescente")

# Executa se nenhuma das condições anteriores for verdadeira
else:
    print("Você é um adulto")
