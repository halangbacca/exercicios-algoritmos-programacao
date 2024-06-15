somatorio = 0

qtd = int(input('Informe a quantidade de números que serão digitados: '))

for i in range(qtd):
    somatorio += int(input('Digite um número: '))

print('Média: ', somatorio / qtd)