a = int(input("Digite o valor do primeiro lado: "))
b = int(input("Digite o valor do segundo lado: "))
c = int(input("Digite o valor do terceiro lado: "))

if (a + b > c) and (a + c > b) and (b + c > a):
    print("Os valores podem formar um triângulo.")
else:
    print("Os valores não podem formar um triângulo.")