numero = int(input("Digite um número: "))

if numero < 1:
    print("O número não é perfeito...")
else:
    soma_divisores = 0
    for i in range(1, numero):
        if numero % i == 0:
            soma_divisores += i

    if soma_divisores == numero:
        print("O número é PERFEITO!")
    else:
        print("O número não é perfeito...")