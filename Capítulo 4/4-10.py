a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
n = int(input("Digite o valor de n: "))

somatorio = 0

for i in range(1, n + 1):
    somatorio += (a - b * i + i)

print(f"O resultado da expressão é {somatorio}.")