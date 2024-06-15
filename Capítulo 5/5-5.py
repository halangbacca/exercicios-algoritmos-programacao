media_pares = 0
media_impares = 0

qtd_pares = 0
qtd_impares = 0

for i in range(1, 11):
    numero = int(input(f"Digite o {i}º número: "))

    if(numero % 2 == 0):
        media_pares += numero
        qtd_pares += 1
    else:
        media_impares += numero
        qtd_impares += 1

print("Média dos pares:", media_pares / qtd_pares)
print("Média dos ímpares:", media_impares / qtd_impares)
