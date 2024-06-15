import random

numero = 1

while numero != 0:
    numero = int(input("Quantos dados devem ser jogados? "))
    if (numero < 1 or numero > 5) and numero != 0:
        print("Quantidade inválida")
    else:
        for i in range(numero):
            print(random.randrange(1, 6))

print("Obrigado por jogar!")