numero = int(input("Digite um número inteiro: "))

numero_original = numero

numero_invertido = 0

while numero > 0:
    ultimo_digito = numero % 10
    numero_invertido = numero_invertido * 10 + ultimo_digito
    numero = numero // 10

print(f"Número original: {numero_original}")
print(f"Número invertido: {numero_invertido}")