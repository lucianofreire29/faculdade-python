# QUESTÃO 4 - Sistema de RH: Média de Desempenho (Setor de RH)
# Fonte: DOC-20261008-WA0207.pdf - Exercício Revisão AV1, exercício 4.
#
# ENUNCIADO
# O RH armazena as últimas 3 notas de desempenho de cada funcionário em um
# dicionário: desempenho = {"Lira": [8, 9, 7], "Paula": [10, 9, 10], "Tiago": [6, 7, 8]}.
# O gestor quer saber a média da funcionária "Paula". Crie um código que:
# 1. Acesse a lista de notas da "Paula".
# 2. Calcule a média das notas (soma das notas dividida pela quantidade de notas).
# 3. Exiba o resultado: "A média de Paula foi [media]".

desempenho = {"Lira": [8, 9, 7], "Paula": [10, 9, 10], "Tiago": [6, 7, 8]}

# O valor associado à chave "Paula" é uma lista com três notas.
notas_paula = desempenho["Paula"]
media = sum(notas_paula) / len(notas_paula)

# :.2f exibe duas casas decimais; a variável mantém o valor calculado.
print(f"A média de Paula foi {media:.2f}")

# RESULTADO ESPERADO
# A média de Paula foi 9.67
# PARA A PROVA: 10 + 9 + 10 = 29; 29 / 3 = 9.6666... (arredondado na exibição).
