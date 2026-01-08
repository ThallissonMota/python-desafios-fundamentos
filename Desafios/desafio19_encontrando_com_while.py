# Solicita a primeira tentativa do usuário
advinhacao = input("Qual será a fruta? ")

# Enquanto a resposta não for "abacate", continua perguntando
while advinhacao.lower() != "abacate":
    advinhacao = input("Qual será a fruta? ")

# Verifica se a resposta final está correta
if advinhacao.lower() == "abacate":
    print("Parabêns! Você acertou a fruta 🎉🎉")
