i = 0
a = 0

inferior_170 = 0
qtd_inferior_170 = 0

maior_20 = 0
qtd_maior_20 = 0

for i in range(5):
    i = int(input("Digite a idade: "))    
    a = int(input("Digite a altura (em centímetros): "))

    if(a < 170):
        inferior_170 += i
        qtd_inferior_170 += 1
    
    if(i > 20):
        maior_20 += a
        qtd_maior_20 += 1

if(qtd_inferior_170 == 0):
    print("Ninguém abaixo de 170 cm")
else:
    print("Idade média dos com altura inferior a 170 cm: ", inferior_170 / qtd_inferior_170)

if(qtd_maior_20 == 0):
    print("Ninguém acima dos 20 anos")
else:
    print("Altura média dos com mais de 20 anos: ", maior_20 / qtd_maior_20)