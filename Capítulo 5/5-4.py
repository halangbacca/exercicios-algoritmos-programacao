maiores_idade = 0

for i in range(1, 11):
    idade = int(input(f"Digite a {i}ª idade: "))

    if(idade >= 18):
        maiores_idade += 1

print(maiores_idade)