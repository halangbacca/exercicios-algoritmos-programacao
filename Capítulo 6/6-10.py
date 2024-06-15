x = float(input("Insira o valor de x: "))

if(abs(x) < 1):
    i = 0
    termo = 0
    serie_anterior = x ** (2 * i + 1)
    serie_atual = x ** (2 * i + 1)

    while(serie_anterior != serie_atual or i <= 1):
        i += 1
        termo = round(x ** (2 * i + 1),15)
        serie_anterior = round(serie_atual,15)
        serie_atual = round(serie_atual + termo,15)

    print("{:.15f}".format(serie_atual))

else:
    print("Valor inválido")