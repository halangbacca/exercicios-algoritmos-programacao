soma = 0
quantidade = 0

while True:
    entrada = input('Digite uma nota (ou <Enter> para sair): ')
    if entrada == '':
        break
    
    nota = float(entrada)

    if nota > 0 and nota <= 10 and nota % 0.5 == 0:
        soma += nota
        quantidade += 1
    else:
        print("Nota inválida")
        break

if quantidade != 0:
    print('Média: ', soma / quantidade)
else:
    print("Nenhuma nota foi digitada")