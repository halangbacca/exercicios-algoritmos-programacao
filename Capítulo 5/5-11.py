numero = int(input("Digite um número: "))

encontrou = False

for num1 in range(1, numero):
    num2 = num1 + 1
    num3 = num1 + 2
    
    produto = num1 * num2 * num3
    
    if produto == numero:
        encontrou = True
        break
    elif produto > numero:
        break

if encontrou:
    print(f"É triangular porque {numero} = {num1} x {num2} x {num3}.")
else:
    print(f"{numero} não é triangular.")
