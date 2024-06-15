valor_arroz = 0

for i in range(0, 64):
    print(2 ** i)
    valor_arroz = 2 ** i

quilos_arroz = valor_arroz // 170000
quilometros_arroz = quilos_arroz // 550000
territorio_brasileiro = quilometros_arroz // 8514876

print('Seriam necessários {} grãos de arroz para efetuar este pagamento'.format(valor_arroz))
print('Seriam necessários {} quilos de arroz para efetuar este pagamento'.format(quilos_arroz))
print('Seria necessário cultivar {} quilômetros quadrados para produzir esta quantidade de arroz'.format(quilometros_arroz))
print('Seria necessário cultivar {} vezes o território brasileiro para produzir esta quantidade de arroz'.format(territorio_brasileiro))