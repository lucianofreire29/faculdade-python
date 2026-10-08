# QUESTÃO 1 - Atualização de Cadastro de Clientes (Setor de CRM)
# Fonte: DOC-20261008-WA0207.pdf - Exercício Revisão AV1, exercício 1.
# Disciplina: Dashboard Analítico em Python - Professor Otonio Castro.
#
# ENUNCIADO
# Você tem um dicionário com o faturamento acumulado de alguns clientes:
# clientes = {"Lira": 5000, "Alon": 3000, "Julia": 4500}.
# O cliente "Alon" fez uma nova compra de R$ 1.500,00. Crie um código que:
# 1. Atualize o valor do cliente "Alon" somando o novo valor ao faturamento antigo.
# 2. Adicione um novo cliente chamado "Marcos" com faturamento inicial de R$ 2.000,00.
# 3. Exiba o dicionário atualizado.

clientes = {"Lira": 5000, "Alon": 3000, "Julia": 4500}

# += soma ao valor existente: equivale a clientes["Alon"] = clientes["Alon"] + 1500.
clientes["Alon"] += 1500

# Atribuir um valor a uma chave nova adiciona esse cliente ao dicionário.
clientes["Marcos"] = 2000

print(clientes)

# RESULTADO ESPERADO
# {'Lira': 5000, 'Alon': 4500, 'Julia': 4500, 'Marcos': 2000}
# PARA A PROVA: usar = 1500 substituiria o faturamento antigo, sem somar a compra.
