def fatorial(n):
    fat = 1
    for i in range(2, n + 1):
        fat *= i
    return fat

def arranjo(n, p):
    a = 1
    for i in range(n-p+1, n+1):
        a *= i
    return a

def combinacao(n, p):
    return arranjo(n, p) // fatorial(p)

print(combinacao(10, 2))
print(combinacao(4, 2))
print(combinacao(30, 1))
print(combinacao(30, 30))