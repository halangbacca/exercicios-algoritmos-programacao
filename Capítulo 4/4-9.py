n = int(input("Digite um número natural n: "))

somatorio = 0

for i in range(1, n + 1):
    somatorio += i ** 2

print(f"O somatório dos quadrados dos números naturais de 1 até {n} é {somatorio}.")