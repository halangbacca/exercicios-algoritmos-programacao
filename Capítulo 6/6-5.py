aplicacao = 10000
preco_carro = 12000

taxa_aplicacao = 0.007
taxa_preco_carro = 0.004

meses = 0

while aplicacao < preco_carro:
    aplicacao += aplicacao * taxa_aplicacao
    preco_carro += preco_carro * taxa_preco_carro
    meses += 1

print(f"Serão necessários {meses} meses para que você tenha dinheiro suficiente para comprar o carro à vista.")