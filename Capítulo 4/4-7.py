valor = int(input('Informe o valor da compra: '))

for i in range(1, 21):
    print('{}x de R$ {}'.format(i, (valor // i)))