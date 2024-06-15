G = 9.80665

altura_pisa = 56
altura_tokyo = 333

tempo_tokyo = (2 * altura_tokyo / G) ** 0.5
tempo_pisa = (2 * altura_pisa / G) ** 0.5

print(f"Tempo de queda da Torre de Pisa (56 metros): {tempo_pisa:.2f} segundos")
print(f"Tempo de queda da Torre de Tóquio (333 metros): {tempo_tokyo:.2f} segundos")