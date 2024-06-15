moeda = input("Digite a sigla da moeda: ")
valor = float(input("Digite o valor em reais: "))

if valor <= 0:
    print("Quantidade inválida")
else:
    if moeda == 'e':
        valor *= 0.31
        print(valor)
    elif moeda == "d":
        valor *= 0.42
        print(valor)
    elif moeda == "m":
        valor *= 5.55
        print(valor)
    elif moeda == 'a':
        valor *= 2.84
        print(valor)
    elif moeda == 'l':
        valor *= 0.26
        print(valor)
    else:
        print("Moeda inválida")