
def analisar_margem (faturamento,custo):
    if faturamento == 0:
        return "nao e possivel calcular a margem de lucro"

    lucro = faturamento - custo
    margem = lucro / faturamento

    if margem >= 0.30:
        return "Margem Saudável"
    else:
        return "Margem Baixa"


print (f"produto de faturamento R$10.000,00 com custo de R$6.000,00, resultado: {analisar_margem(10000,6000)} ")
