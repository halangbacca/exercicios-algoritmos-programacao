populacao_inicial = 1000000
populacao_atual = populacao_inicial

mortes = 0
nascimentos = 0
    
# Ano inicial
ano = 1600
    
# Enquanto a população atual for maior ou igual a 10% da inicial
while populacao_atual >= 0.1 * populacao_inicial:
    # Calcular número de mortes no ano (6% da população no início do ano)
    mortes += int(populacao_atual * 0.06)
        
    # Calcular número de nascimentos que sobreviveram (1% da população inicial)
    nascimentos += int(populacao_inicial * 0.01)
        
    # População no final do ano
    populacao_atual = populacao_atual - mortes + nascimentos
        
    # Imprimir informações do ano
    print(f"Ano: {ano} - Nascimentos: {nascimentos} - Mortes: {mortes} - População atual: {populacao_atual}")
        
    # Incrementar o ano
    ano += 1