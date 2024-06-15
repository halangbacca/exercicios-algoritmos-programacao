x = float(input("Digite o valor de x: "))

termo = x 
seno = termo
n = 1
precisao = 1e-10

while abs(termo) > precisao:
    termo = -termo * x * x / ((2 * n) * (2 * n + 1))
    seno += termo
    n += 1

print(f"O seno de {x} é aproximadamente {seno:.10f}")