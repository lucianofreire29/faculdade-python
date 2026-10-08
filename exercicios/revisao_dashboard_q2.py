# QUESTÃO 2 - Consulta de Estoque Interativa (Setor de Logística)
# Fonte: DOC-20261008-WA0207.pdf - Exercício Revisão AV1, exercício 2.
#
# ENUNCIADO
# A empresa possui o seguinte estoque:
# estoque = {"teclado": 50, "mouse": 120, "monitor": 30}.
# Crie um programa que peça para o usuário digitar o nome de um produto.
# 1. Se o produto existir no estoque, exiba a quantidade disponível.
# 2. Se o produto não existir, exiba: "Produto não encontrado no sistema".
# Obs.: trate o input para evitar erros de letras maiúsculas ou espaços.

estoque = {"teclado": 50, "mouse": 120, "monitor": 30}

# input() recebe texto. strip() remove espaços nas pontas; lower() deixa minúsculo.
produto = input("Digite o nome do produto: ").strip().lower()

# in verifica se a CHAVE existe antes de acessar seu valor com [produto].
if produto in estoque:
    print(f"Quantidade disponível de {produto}: {estoque[produto]}")
else:
    print("Produto não encontrado no sistema")

# EXEMPLOS (a mensagem aparece depois do pedido de entrada)
# Entrada: "  MOUSE  " -> Quantidade disponível de mouse: 120
# Entrada: "impressora" -> Produto não encontrado no sistema
# PARA A PROVA: uma chave inexistente acessada diretamente causaria KeyError.
