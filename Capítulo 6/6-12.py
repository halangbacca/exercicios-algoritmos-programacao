x = float(input("Digite o valor de x: "))

termo = 1
cosseno = termo
n = 1
precisao = 1e-10

while abs(termo) > precisao:
    termo = -termo * x * x / ((2 * n - 1) * (2 * n))
    cosseno += termo
    n += 1

print(f"O cosseno de {x} é aproximadamente {cosseno:.10f}")