def imprimir_triangulo(n, linha_atual = 1):
    if linha_atual > n:
        return
    else:
        print('$' * linha_atual)
        imprimir_triangulo(n, linha_atual + 1)

imprimir_triangulo(5)