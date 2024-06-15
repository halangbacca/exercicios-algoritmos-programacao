contador = 0

dividendo = int(input("Digite o valor do dividendo: "))
divisor = int(input("Digite o valor do dividor: "))

while dividendo >= divisor:
    dividendo -= divisor
    contador += 1

print("Divisão: ", contador)
print("Resto: ", dividendo)