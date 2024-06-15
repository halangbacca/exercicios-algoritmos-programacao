numero = int(input('Digite um número: '))
e_primo = True

for possivel_divisor in range(2, numero // 2 + 1):
    print("Divisor: ", possivel_divisor)
    if numero % possivel_divisor == 0:
        e_primo = False

if e_primo:
    print(f'{numero} é um número primo!')
else:
    print(f'{numero} não é um número primo!')