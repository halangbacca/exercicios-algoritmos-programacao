def fatorial(n):
    fat = 1
    for i in range(2, n + 1):
        fat *= i
    return fat

n = int(input('Digite o valor de n: '))
p = int(input('Digite o valor de p: '))

saida = fatorial(n) // (fatorial(p) * fatorial(n - p))
print(f'C({n},{p}): {saida}')