vantagem_tartaruga = int(input("Digite o valor da distância de vantagem da tartaruga: "))
velocidade_tartaruga = int(input("Digite o valor da velocidade da tartaruga: "))
velocidade_lebre = int(input("Digite o valor da velocidade da lebre: "))

tempo = vantagem_tartaruga / (velocidade_lebre - velocidade_tartaruga)

if tempo < 0:
    print(f"A lebre nunca alcançará a tartaruga.")
else:
    print(f"A lebre levará aproximadamente {tempo:.2f} minutos para alcançar a tartaruga.")