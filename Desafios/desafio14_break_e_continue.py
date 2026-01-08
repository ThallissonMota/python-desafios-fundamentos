# Variáveis inicializadas
num = 1
num2 = 1

# Loop de 1 até 10
for numero in range(1, 11):
    # break encerra o loop quando a condição é verdadeira
    if numero > 5:
        break
    print(numero)
    numero += 1  

print("\n---------------\n")

# Loop de 1 até 10
for numero in range(1, 11):
    # continue pula a iteração atual e segue o loop
    if numero == 5:
        continue
    print(numero)
    numero += 1  
