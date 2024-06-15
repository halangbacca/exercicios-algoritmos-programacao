salario = 2000.0
aumento_salarial = 0.05 # 5% de aumento anual em março
divida = 100.0
taxa_juros = 0.15   # 15% de juros ao mês
mes = 10    # Outubro
ano = 2016
    
while divida <= salario:
    # Verifica se o mês é março para aumentar o salário
    if mes == 3:
        salario *= (1 + aumento_salarial)
        
    divida *= (1 + taxa_juros)
    
    # Verifica se a dívida acumulada ultrapassou o salário
    if divida > salario:
        print(f"A dívida de Pedro será superior ao seu salário em {mes}/{ano}.")
        break
        
    # Incrementa o mês
    mes += 1
    
    # Se passou de dezembro, incrementa o ano e volta para janeiro (mês 1)
    if mes > 12:
        mes = 1
        ano += 1