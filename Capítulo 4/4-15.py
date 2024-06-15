n = int(input("Digite um número: "))

if n <= 0:
    print("O número deve ser maior que zero.")
elif n == 1:
    print(0)
elif n == 2:
    print(1)
else:
    a, b = 0, 1
    
    for _ in range(2, n):
        a, b = b, a + b

    print(b)