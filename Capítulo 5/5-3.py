qualidade = int(input("Digite a nota de qualidade: "))
preco = int(input("Digite a nota de preço: "))
prazo = int(input("Digite a nota de prazo: "))

if qualidade < 7:
    print(0)
elif qualidade >= 7 and preco >= 7:
    print((qualidade + preco + prazo) / 3)
elif qualidade >= 7 and preco < 7:
    print((qualidade + 2 * preco + prazo) / 4)