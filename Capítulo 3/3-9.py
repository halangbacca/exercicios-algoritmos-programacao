altura = int(input("Digite a altura: "))
comprimento = int(input("Digite a largura: "))
largura = int(input("Digite a largura: "))

print("Área da sala: ", largura * comprimento)
print("Volume: ", altura * comprimento * largura)
print("Área das paredes: ", 2 * altura * largura + 2 * altura * comprimento)