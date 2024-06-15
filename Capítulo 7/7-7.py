def imprimir_triangulo_invertido(n):
    if n == 0:
        return
    else:
        print('$' * n)
        imprimir_triangulo_invertido(n - 1)

imprimir_triangulo_invertido(3)