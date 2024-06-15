valor_compra = float(input("Digite o valor da compra em R$: "))

valor_a_vista = valor_compra * 0.91
valor_prestacao_5 = valor_compra / 5
valor_prestacao_10 = (valor_compra * 1.17) / 10

print(f"Valor à vista R$: {valor_a_vista:.1f}")
print(f"Valor da prestação em 5 vezes R$: {valor_prestacao_5:.1f}")
print (f"Valor da prestação em 10 vezes R$: {valor_prestacao_10:.1f}")