# Verificar se o ano é bissexto
def e_bissexto(ano):
    if ano % 4 == 0:
        if ano % 100 == 0:
            if ano % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

# Entrada dos valores pelo usuário
dia = int(input("Digite o dia: "))
mes = int(input("Digite o mês: "))
ano = int(input("Digite o ano: "))
dias_para_adicionar = int(input("Digite a quantidade de dias a serem somados: "))

# Dicionário de dias por mês, considerando bissexto ou não
dias_no_mes = {
    1: 31,  # Janeiro
    2: 29 if e_bissexto(ano) else 28,  # Fevereiro (considerando ano bissexto)
    3: 31,  # Março
    4: 30,  # Abril
    5: 31,  # Maio
    6: 30,  # Junho
    7: 31,  # Julho
    8: 31,  # Agosto
    9: 30,  # Setembro
    10: 31,  # Outubro
    11: 30,  # Novembro
    12: 31   # Dezembro
}

# Adiciona os dias ao dia atual
dia += dias_para_adicionar

# Loop para ajustar a data enquanto o dia for maior que os dias no mês atual
for mes in range(mes, 13):  # Percorre os meses a partir do mês atual até dezembro
    if dia > dias_no_mes[mes]:
        dia -= dias_no_mes[mes]
    else:
        break
    if mes == 12:  # Se chegou em dezembro, avança o ano
        ano += 1
        mes = 0  # Reinicia o mês para janeiro

# Exibir a nova data
print(f"A nova data é: {dia:02}/{mes:02}/{ano}")

# O código acima pode ser resumido utilizando as bibliotecas date e timedelta
    # from datetime import date, timedelta

    # dia = int(input("Digite o dia: "))
    # mes = int(input("Digite o mês: "))
    # ano = int(input("Digite o ano: "))
    # dias_para_adicionar = int(input("Digite a quantidade de dias a serem adicionados: "))

    # data_atual = date(ano, mes, dia)
    # print(data_atual + timedelta(days = dias_para_adicionar))