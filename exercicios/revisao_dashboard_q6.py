# QUESTÃO 6 - Performance de Vendas Regionais (Setor de Dashboard)
# Fonte: DOC-20261008-WA0208.pdf - Revisão 02, exercício 1.
#
# ENUNCIADO
# Crie uma função chamada analisar_vendas que receba uma lista de números (vendas).
# A função deve retornar o total vendido e a média das vendas.
# Dado o dicionário:
# dados_filiais = {"Matriz": [10000, 15000, 20000], "Filial Sul": [5000, 7000]}:
# 1. Percorra o dicionário.
# 2. Para cada filial, use a função e faça o unpacking do resultado.
# 3. Exiba: "Filial [Nome] -> Total: R$[valor], Média: R$[valor]".


def analisar_vendas(vendas):
    # Como nos dados do enunciado, a lista deve conter pelo menos uma venda.
    total = sum(vendas)
    media = total / len(vendas)

    # A vírgula agrupa os dois resultados em uma tupla: (total, media).
    return total, media


dados_filiais = {"Matriz": [10000, 15000, 20000], "Filial Sul": [5000, 7000]}

# Percorrer o dicionário fornece suas chaves: "Matriz" e "Filial Sul".
for filial in dados_filiais:
    vendas_filial = dados_filiais[filial]

    # Unpacking (desempacotamento): cada variável recebe um dos retornos, na ordem.
    total, media = analisar_vendas(vendas_filial)
    print(f"Filial {filial} -> Total: R${total:.2f}, Média: R${media:.2f}")

# RESULTADO ESPERADO
# Filial Matriz -> Total: R$45000.00, Média: R$15000.00
# Filial Filial Sul -> Total: R$12000.00, Média: R$6000.00
# "Filial Filial Sul" segue o modelo pedido e o nome da chave fornecida no PDF.
# PARA A PROVA: return entrega os resultados; print apenas mostra na tela.
