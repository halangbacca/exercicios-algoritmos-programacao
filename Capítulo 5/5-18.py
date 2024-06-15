peso = float(input("Digite o peso: "))
altura = float(input("Digite a altura: "))

imc = peso / (altura ** 2)

if imc < 18.5:
    print("Adulto com baixo peso")
elif imc >= 18.5 and imc < 25:
    print("Adulto com peso adequado")
elif imc >= 25 and imc < 30:
    print("Adulto com sobrepeso")
elif imc >= 30:
    print("Adulto com obesidade")