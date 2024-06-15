valor_inicial = int(input('Entre com o valor inicial: '))

for i in range(valor_inicial, -1, -1):
    print(i)

print('Fogo!')

# Quando o usuário digita zero:
    # Entrada do usuário: valor_inicial = 0
    # O loop for é inicializado com range(0, -1, -1).
    # Este range começa em 0 e termina em -1 (exclusivo), decrementando de 1 em 1.
    # Portanto, ele só inclui o número 0.
    # O loop executa uma vez, imprimindo 0.
    # Após a conclusão do loop, o programa imprime 'Fogo!'.

# Quando o usuário digita um valor negativo:
    # Entrada do usuário: valor_inicial = -1 (ou qualquer outro valor negativo)
    # O loop for é inicializado com range(-1, -1, -1) (ou outro range que começa em um valor negativo e vai até um valor menor).
    # Para qualquer valor negativo fornecido, o loop for não terá nenhum número para iterar, pois o início do range já é menor ou igual ao final do range.
    # Como não há números no range para iterar, o corpo do loop for não é executado.
    # O programa vai diretamente para a impressão de 'Fogo!'.