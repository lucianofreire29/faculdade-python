# QUESTÃO 3 - Análise de Faturamento por Região (Setor Financeiro)
# Fonte: DOC-20261008-WA0207.pdf - Exercício Revisão AV1, exercício 3.
#
# ENUNCIADO
# Dada a lista de faturamento por região:
# vendas_regiao = {"Norte": 15000, "Sul": 22000, "Leste": 18000, "Oeste": 25000}.
# Seu programa deve:
# 1. Extrair todos os valores (faturamentos) para uma lista.
# 2. Calcular e exibir o faturamento total da empresa (soma de todas as regiões).
# 3. Calcular e exibir o faturamento médio das regiões.
# Observação: apesar de o texto dizer "lista", os dados fornecidos são um dicionário.

vendas_regiao = {"Norte": 15000, "Sul": 22000, "Leste": 18000, "Oeste": 25000}

# values() fornece os valores; list() transforma esses valores em uma lista.
faturamentos = list(vendas_regiao.values())
total = sum(faturamentos)

# São quatro regiões: média = 80000 / 4 = 20000.
media = total / len(faturamentos)

print(f"Faturamentos: {faturamentos}")
print(f"Faturamento total: R$ {total:.2f}")
print(f"Faturamento médio: R$ {media:.2f}")

# RESULTADO ESPERADO
# Faturamentos: [15000, 22000, 18000, 25000]
# Faturamento total: R$ 80000.00
# Faturamento médio: R$ 20000.00
# PARA A PROVA: list(vendas_regiao) obteria as chaves, e não os faturamentos.
