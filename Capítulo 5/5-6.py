soma_pares = 0
soma_impares = 0

qtd_pares = 0
qtd_impares = 0

media_pares = 0
media_impares = 0

for i in range(1, 11):
    numero = int(input(f"Digite o {i}º número: "))

    if(numero % 2 == 0 and numero != 0):
        soma_pares += numero
        qtd_pares += 1
    else:
        soma_impares += numero
        qtd_impares += 1

if(soma_pares == 0):
    print("Nenhum número par")
else:
    media_pares = soma_pares / qtd_pares
    print("Média dos pares:", media_pares)

if(soma_impares == 0):
    print("Nenhum número ímpar")
else:
    media_impares = soma_impares / qtd_impares
    print("Média dos ímpares:", media_impares)

