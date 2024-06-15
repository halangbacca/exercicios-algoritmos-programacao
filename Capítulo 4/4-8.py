inferior = int(input("Digite o valor do limite inferior: "))
superior = int(input("Digite o valor do limite superior: "))

# Se os limites estiverem invertidos, corrige a ordem
if inferior > superior:
    inferior, superior = superior, inferior

# Calcula o somatório usando a fórmula da soma de uma progressão aritmética
n = superior - inferior + 1
somatorio = (n * (inferior + superior)) // 2

print(f"O somatório dos números inteiros entre {inferior} e {superior} é {somatorio}.")
