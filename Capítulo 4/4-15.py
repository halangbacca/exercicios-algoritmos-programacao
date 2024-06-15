numero = int(input("Digite um número: "))

sequencia_fibonacci = [0, 1]

while len(sequencia_fibonacci) <= numero:
    sequencia_fibonacci.append(sequencia_fibonacci[-1] + sequencia_fibonacci[-2])

print(sequencia_fibonacci[-1])