nota = float(input("Digite uma nota: "))

if nota >= 9 and nota <= 10:
    print("A")
elif nota >= 8 and nota <= 8.999:
    print("B")
elif nota >= 7 and nota <= 7.999:
    print("C")
elif nota < 7 and nota >= 0:
    print("E")
else:
    print("Nota inválida")